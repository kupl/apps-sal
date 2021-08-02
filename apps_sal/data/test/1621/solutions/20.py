s = input()
n = int(input())
a = list(map(int, input().split()))
mx = max(a)
ans = 0
for i in range(len(s)): ans += (a[ord(s[i]) - ord('a')] * (i + 1))
for i in range(len(s) + 1, len(s) + n + 1): ans += (mx * i)
print(ans)
