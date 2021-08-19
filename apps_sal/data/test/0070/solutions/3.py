s = input().split()
k = int(s[1])
n = s[0]
ptr = len(s[0]) - 1
zerocount = 0
ans = 0
while ptr >= 0 and zerocount < k:
    if n[ptr] == '0':
        zerocount += 1
    else:
        ans += 1
    ptr -= 1
if ptr == -1:
    print(len(n) - 1)
else:
    print(ans)
