N = int(input())
a = list(map(int, input().split()))
ans = [0 for i in range(N + 1)]

for i in range(N, 0, -1):
    res = 0
    for j in range(1, N + 1):
        if i * j > N:
            break
        else:
            res += ans[i * j]

    if res % 2 != a[i - 1]:
        ans[i] += 1

print((sum(ans)))
A = []
for i, v in enumerate(ans):
    if v > 0:
        A.append(i)


print((*A))
