

inp1 = input().split()
n = int(inp1[0])
k = int(inp1[1])

s = input()


def isGood(l):
    if(l == 0):
        return True
    s1 = s[0:l]
    s2 = s[n - l:n]
    return s1 == s2


maxMatch = 0

for i in range(n - 1, 0, -1):
    if isGood(i):
        maxMatch = i
        break

ans = ""
for i in range(k):
    if(i == 0):
        ans += s
    else:
        ans += s[maxMatch:n]

print(ans)
