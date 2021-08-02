N, K, Q = map(int, input().split())
S = [(K - Q) for i in range(N)]

for _ in range(Q):
    i = int(input())
    S[i - 1] += 1

for n in S:
    if n > 0:
        print("Yes")
    else:
        print("No")
