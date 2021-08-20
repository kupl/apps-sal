Q = int(input())
for _ in range(Q):
    n = int(input())
    zs = 0
    os = 0
    odd = 0
    for k in range(n):
        s = input()
        zs += s.count('0')
        os += s.count('1')
        odd += len(s) % 2
    if zs % 2 == 1 and os % 2 == 1 and (odd == 0):
        print(n - 1)
    else:
        print(n)
