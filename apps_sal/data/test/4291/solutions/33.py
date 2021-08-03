N, Q = list(map(int, input().split()))
S = input()

total = [0] * N
for i in range(1, N):
    total[i] = total[i - 1]
    if S[i - 1] == 'A' and S[i] == 'C':
        total[i] += 1

for q in range(Q):
    L, R = list(map(int, input().split()))
    L -= 1
    R -= 1

    count = total[R] - total[L]
    print(count)
