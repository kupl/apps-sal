n = int(input())

st = {}

while not n in st:
    st[n] = True
    n += 1
    while n % 10 == 0:
        n /= 10

print(len(st))
