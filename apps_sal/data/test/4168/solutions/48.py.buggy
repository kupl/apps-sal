N = int(input())
if N == 0:
    print(0)
    return

ans = ''
while N != 1:
    d = N % 2
    ans += str(d)
    N -= d
    N //= -2
ans += '1'
print(ans[::-1])
