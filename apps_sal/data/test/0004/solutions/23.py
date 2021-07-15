

x = list(map(int, input().strip().split()))[0]
h, m = list(map(int, input().strip().split()))


count = 0

while True:
    a = str(h)
    b = str(m)
    if '7' in a:
        break
    if '7' in b:
        break
    count += 1
    m -= x
    if m < 0:
        h -= 1
        m += 60
    if h < 0:
        h += 24

print(count)
