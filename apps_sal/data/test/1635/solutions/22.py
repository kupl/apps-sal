n = int(input())
s = [200001] * 200001
a = list(map(int, input().split()))
for i in range(1, n + 1):
    s[a[i - 1]] = i - 1
ans = s.index(min(s))
print(ans)
