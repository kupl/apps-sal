t = int(input())
for _ in range(t):
    n = input()
    s = len(n)
    n = int(n)
    su = (s - 1) * 9
    q = '1' * s
    q = int(q)
    print(su + n // q)
