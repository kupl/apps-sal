(x, n) = list(map(int, input().split()))
p = list(map(int, input().split()))
a = 0
while True:
    if x - a not in p:
        print(x - a)
        break
    elif x + a not in p:
        print(x + a)
        break
    a += 1
