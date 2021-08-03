N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

a = [0] * (N + 1)
b = [0] * (N + 1)
for i in range(N):
    a[A[i]] += 1
    b[B[i]] += 1

ok = True
for i in range(1, N + 1):
    if a[i] + b[i] > N:
        ok = False

sa = [0] * (N + 1)
sb = [0] * (N + 1)
for i in range(N):
    sa[i + 1] = sa[i] + a[i + 1]
    sb[i + 1] = sb[i] + b[i + 1]

ans = 0
for i in range(N):
    ans = max(ans, sa[i + 1] - sb[i])

if ok:
    print("Yes")
    for i in range(N):
        print(B[(i + N - ans) % N], end='')
        if i == N - 1:
            print('')
        else:
            print(' ', end='')
else:
    print("No")
