def all_outcome(x, y, a, b):
    s = x + y
    outcomes = []
    for c in range(a, x + 1):
        for d in range(b, y + 1):
            if d >= b and d <= y and (c > d):
                outcomes.append([c, d])
    print(len(outcomes))
    for o in outcomes:
        print(o[0], o[1])


l = input().split()
x = int(l[0])
y = int(l[1])
a = int(l[2])
b = int(l[3])
all_outcome(x, y, a, b)
