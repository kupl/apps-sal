A = int(input())
az = 'zabcdefghijklmnopqrstuvwxy'
ans = ''
abc = 'abcdefghijklmnopqrstuvwxyz'
while A:
    A -= 1
    ans = abc[A % 26] + ans
    A = A // 26
print(ans)
