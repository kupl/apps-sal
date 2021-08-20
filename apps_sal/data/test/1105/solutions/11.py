import sys
f = sys.stdin
n = int(f.readline().strip())
people = {}
res = 'YES'
for i in range(n):
    (x, k) = list(map(int, f.readline().strip().split()))
    if k in people:
        if x == people[k] + 1:
            people[k] = x
        elif x <= people[k]:
            pass
        else:
            res = 'NO'
            break
    elif x == 0:
        people[k] = x
    else:
        res = 'NO'
        break
print(res)
