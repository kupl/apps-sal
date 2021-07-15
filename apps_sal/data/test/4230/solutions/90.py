x, n = [int(s) for s in input().split()]
p_set = set([int(s) for s in input().split()])
a = 0
while True:
    for i in [-1, 1]:
        y = x + i * a
        if y not in p_set:
            print(y)
            return
    a += 1
