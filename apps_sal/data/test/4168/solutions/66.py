# C - Base -2 Number

N = int(input())

ans = ''
if N == 0:
    ans = '0'
while N != 0:
    if N % 2 == 1:
        ans = '1' + ans
        N -= 1
    else:
        ans = '0' + ans
    N //= -2
print(ans)
