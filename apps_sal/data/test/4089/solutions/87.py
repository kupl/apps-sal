N = int(input())

az = 'abcdefghijklmnopqrstuvwxyz'
ans = ''

while N:
    N -= 1
    ans = az[N%26] + ans
    N = N // 26

print(ans)
