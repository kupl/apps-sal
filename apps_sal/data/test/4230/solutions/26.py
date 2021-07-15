x, n = [int(s) for s in input().split()]
p_set = set([int(s) for s in input().split()])
a = 0
while True:
    if x - a not in p_set:
        print(x - a)
        break
    if x + a not in p_set:
        print(x + a)
        break
    a += 1
