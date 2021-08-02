def s(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


n = int(input())
if n % s(n) == 0: print("Yes")
else: print("No")
