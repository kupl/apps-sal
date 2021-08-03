n = int(input())
if n == 0:
    print(0)
    return
ans = ""
while n != 0:
    r = n % 2
    if r < 0:
        r += 2
    ans += str(r)
    n = (n - r) // (-2)
print(ans[::-1])
