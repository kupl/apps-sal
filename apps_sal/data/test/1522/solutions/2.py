n = int(input())
a = [0 for i in range(26)]
s = input().strip()
ans = 0
for i in range(n - 1):
    a[ord(s[2 * i]) - 97] += 1
    if a[ord(s[2 * i + 1]) - 65] > 0:
        a[ord(s[2 * i + 1]) - 65] -= 1
    else:
        ans += 1
print(ans)
