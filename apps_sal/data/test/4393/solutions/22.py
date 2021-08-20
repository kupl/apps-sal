n = int(input())
s = input().strip()
ans = ''
i = 0
k = 1
while i < n:
    ans += s[i]
    i += k
    k += 1
print(ans)
