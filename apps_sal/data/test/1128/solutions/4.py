a, m = list(map(int, input().split()))
s = set()
while True:
    a %= m
    if a in s:
        print('Yes' if 0 in s else 'No')
        break
    s.add(a)
    a *= 2

