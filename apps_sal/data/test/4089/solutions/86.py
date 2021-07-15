n = int(input())
alphabets = [chr(i) for i in range(ord('a'), ord('a') + 26)]
ans = ''
while n > 0:
    n -= 1
    ans += alphabets[n % 26]
    n //= 26
print(ans[::-1])
