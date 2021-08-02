n = int(input())
nuts = list(map(str, input().split()))
ans = 1
cur = 1
isone = False
for i in range(n):
    if nuts[i] == '1':
        isone = True
        ans *= cur
        cur = 1
    else:
        if isone:
            cur += 1
if isone:
    print(ans)
else:
    print(0)
