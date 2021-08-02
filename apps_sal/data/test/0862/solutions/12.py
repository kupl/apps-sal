n = int(input())
a = [int(v) for v in input().split()]

a = [ai - i for i, ai in enumerate(a)]

minv = 100000000000000
mini = None

for i, ai in enumerate(a):
    if ai <= 0:
        print(i + 1)
        return
    else:
        v = (ai - 1) // n
        if v < minv:
            minv = v
            mini = i

print(mini + 1)
