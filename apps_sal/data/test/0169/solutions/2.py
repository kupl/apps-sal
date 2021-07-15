n = int(input())
a = int(input())
b = int(input())
c = int(input())
if a <= b - c or b > n:
    print(n // a)
else:
    ans = (n - c) // (b - c)
    ans += ((n - c) % (b - c) + c) // a
    print(ans)
