N = int(input()) - 1

char = list('abcdefghijklmnopqrstuvwxyz')


ans = ''
i = N % 26
N //= 26
ans = char[i] + ans
while N > 0:
    N -= 1
    i = N % 26
    N //= 26
    ans = char[i] + ans

print(ans)
return
