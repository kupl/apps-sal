h, a = map(int,input().split())

c = 0
while h > 0:
    h -= a
    c += 1

print(c)
