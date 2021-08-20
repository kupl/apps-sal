n = int(input())
nums = []
ans = ''
while n >= 1:
    n -= 1
    ans += chr(ord('a') + n % 26)
    n = n // 26
print(ans[::-1])
