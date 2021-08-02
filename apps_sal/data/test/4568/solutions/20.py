n = int(input())
s = str(input())

ans = 0
for i in range(1, n):
    be_s = set(s[:i])
    af_s = set(s[i:])
    num = len(be_s & af_s)
    ans = max(ans, num)

print(ans)
