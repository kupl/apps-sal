(h, a) = map(int, input().split())
count = 0
if h % a != 0:
    print(int(h // a) + 1)
else:
    print(int(h / a))
