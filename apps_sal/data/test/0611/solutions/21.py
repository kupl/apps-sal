# def Bob(pos,x,d,a):
#     pos -= 1
#     for i in range(len(a)):
#         a[i] += x + d*abs(i-pos)
#     return a

def main():
    n, m = [int(x) for x in input().split()]
    a = [0] * n
    xx = 0
    dd = 0

    for _ in range(m):
        x, d = [int(x) for x in input().split()]
        xx += x * n
        if d > 0:
            dd += d * (n * (n - 1)) // 2
        else:
            z = (n + 1) // 2
            dd += d * (z * (z - 1))
            if n % 2 == 0:
                dd += (n // 2) * d
    print((xx + dd) / n)


main()
