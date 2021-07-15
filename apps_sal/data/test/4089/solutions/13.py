N = int(input())
ans = ''
while N:
    N -= 1
    N, mod = divmod(N, 26)
    ans += chr(ord('a') + mod)
print(ans[::-1])
