k, r = list(map(int, input().split()))

for a in range(1, 11):
    price = (k * a) % 10
    if price == r or price == 0:
        print(a)
        break
