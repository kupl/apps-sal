n, b, p = [int(x) for x in input().split()]
b1, p1 = 0, n*p
while n > 1:
    n1 = 2 << (n.bit_length()-2)
    b1 += (2*b + 1) * n1 // 2
    n -= n1//2
print(b1, p1)

