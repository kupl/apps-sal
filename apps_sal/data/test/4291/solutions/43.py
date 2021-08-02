N, Q = map(int, input().rstrip().split())
S = input().rstrip()
a = [0] * N
for i in range(N):
    if i > 1:
        a[i] = a[i - 1]
    if i != 0 and S[i - 1] == 'A' and S[i] == 'C':
        a[i] += 1
for _ in range(Q):
    l, r = map(int, input().rstrip().split())
    print(a[r - 1] - a[l - 1])
