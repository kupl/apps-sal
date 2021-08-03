N, K, Q = list(map(int, input().split()))

if K > Q:
    for i in range(N):
        print("Yes")
    return

T = [0 for i in range(N)]
t = Q - K

for i in range(Q):
    a = int(input())
    T[a - 1] += 1

for i in range(N):
    if T[i] > t:
        print("Yes")
    else:
        print("No")
