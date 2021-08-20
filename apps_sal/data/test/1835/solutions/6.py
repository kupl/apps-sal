Q = int(input())
for _ in range(Q):
    n = int(input())
    (zero, one) = (0, 0)
    odd = 0
    for _ in range(n):
        s = input()
        if len(s) % 2:
            odd = 1
        zero += s.count('0')
        one += s.count('1')
    if odd or zero % 2 == 0:
        print(n)
    else:
        print(n - 1)
