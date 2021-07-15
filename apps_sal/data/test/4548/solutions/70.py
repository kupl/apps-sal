n, m, x = map(int, input().split())

back = 0
for a in map(int, input().split()):
    if a < x:
        back += 1
else:
    print(min(back, m - back))
