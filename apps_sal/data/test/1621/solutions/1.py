s = input().strip()
k = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(len(s)):
    ans += (i + 1) * a[(ord(s[i]) - 97)]
m = max(a)
for i in range(len(s), len(s) + k):
    ans += m * (i + 1)
print(ans)
