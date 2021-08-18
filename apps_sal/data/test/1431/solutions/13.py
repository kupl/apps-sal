N = int(input())
a = list(map(int, input().split()))

A = [0] + a
B = [0] * (N + 1)
ans = []

for i in range(N, 0, -1):
    tmp = 0
    for j in range(i * 2, N + 1, i):
        tmp += B[j]

    if tmp % 2 != A[i]:
        B[i] = 1
        ans.append(i)

if len(ans) == 0:
    print((0))
else:
    print((len(ans)))
    print((' '.join(map(str, ans))))
