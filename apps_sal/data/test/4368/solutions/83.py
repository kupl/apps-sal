n, k = map(int, input().split())

m = 0
while True:
    m += 1
    if k**m > n:
        print(m)
        break
