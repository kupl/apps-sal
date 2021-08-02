

n = int(input())
ans = ''

if (n % 2 != 0):
    ans += '7'
    n -= 3

while (n >= 2):
    ans += '1'
    n -= 2

print(ans)
