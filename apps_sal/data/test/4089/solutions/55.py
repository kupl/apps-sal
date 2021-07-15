n = int(input())

s = "abcdefghijklmnopqrstuvwxyz"
ans = ''
while n > 0:
    n -= 1
    ans = s[n % 26] + ans
    #Floor division
    n //= 26
print(ans)
