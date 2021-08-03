def read(): return list(map(int, input().split()))


n, m = int(input()), int(input())
if n < 100:
    print(m % (2**n))
else:
    print(m)
