[n, r] = input().split()
n = int(n)
r = int(r)
if n >= 10:
    print(r)
else:
    ans = r + 100 * (10 - n)
    print(ans)
