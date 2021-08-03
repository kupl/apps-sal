n = int(input())
ans = ''
while n != 0:
    r = n % 2
    n = (n - r) // (-2)
    ans += str(r)
print(ans[::-1] if ans else 0)
