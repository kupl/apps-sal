_ , X = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]

o = len(s)
s = [x for x in s if x >= 0]

acc = o - len(s)

if X in s: acc += 1
s = [x for x in s if x < X]

acc += X - len(s)

print(acc)

