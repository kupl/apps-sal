def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

s = input().strip()
n = len(s)
s += s
p = ans = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        p = 1
    else:
        p += 1
        ans = max(ans, p)
ans = min(ans, n)
print(ans)

