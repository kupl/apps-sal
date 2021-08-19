(a, b, k) = map(int, input().split())
ans = []
for i in reversed(range(1, 101)):
    if b % i == 0 and a % i == 0:
        ans.append(i)
print(ans[k - 1])
