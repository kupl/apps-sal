N, Q = map(int, input().split())
S = input()

a = [0] * N
c = 0

for i in range(N-1):
    if S[i:i+2] == "AC":
        c += 1
    a[i + 1] = c

l = [0] * Q
r = [0] * Q
for i in range(Q):
    l[i], r[i] = map(int, input().split())
for i in range(Q):
    print(a[r[i] - 1] - a[l[i] - 1])
