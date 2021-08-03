n = int(input())
a = int(input())
b = int(input())
c = int(input())
if n == 1:
    print(0)
else:
    ans = min(a, b)
    n -= 2
    if a <= b:
        ans = ans + n * min(a, c)
    else:
        ans = ans + n * min(b, c)
    print(ans)
