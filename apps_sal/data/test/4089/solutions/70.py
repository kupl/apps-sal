n = int(input())
ans = ''

while(n):
    n -= 1
    #print('value:',ord('a') + n % 26)
    ans += chr(ord('a') + n % 26)
    n //= 26

print(("".join(list(ans[::-1]))))

