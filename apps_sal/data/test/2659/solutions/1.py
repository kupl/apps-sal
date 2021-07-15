def S(n):
    return sum(map(int, str(n)))


K = int(input())

x = 1
d = 1
while K > 0:
    if S(x) * d < x:
        x += 9 * d
        d *= 10
    else:
        print(x)
        x += d
        K -= 1
