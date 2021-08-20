n = int(input())
a = list(map(int, input().split()))
x = sum([a[i] * (-1) ** (i % 2) for i in range(n)])
ans = [x]
for i in range(n - 1):
    ans.append(2 * a[i] - ans[-1])
print(' '.join(map(str, ans)))
