n = int(input())
ans = ''
while n:
    n -= 1
    ans += chr(n % 26 + 97)
    n = n // 26
print(*ans[::-1], sep='')
