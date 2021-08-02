na = list(map(int, input().split()))
s = input()

n = na[0]
k = na[1]

amk = 0
s = sorted(s)
last = -2
ans = 0
amdone = 0

for i in range(len(s)):
    if amdone == k:
        break
    if k + amk > n:
        print(-1)
        return
    if ord(s[i]) - 96 > last + 1:
        last = ord(s[i]) - 96
        ans += ord(s[i]) - 96
        amdone += 1
    else:
        amk += 1

if k + amk > n:
    print(-1)
else:
    print(ans)
