A = int(input())
az = 'zabcdefghijklmnopqrstuvwxy'
ans = ''
while A / 26 > 0:
    ans = az[A % 26] + ans
    A = (A - 1) // 26
print(ans)
