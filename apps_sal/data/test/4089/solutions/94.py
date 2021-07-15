N = int(input())

ans = ''

while(N):
    N -= 1
    ans = ans + chr(int(N % 26) + 97)
    N = N // 26
ans = ''.join(list(reversed(ans)))
print(ans)

