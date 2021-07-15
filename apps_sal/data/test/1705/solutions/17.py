n = int(input())
l = [*map(int, input().split())]
z = l.count(0)
o = l.count(1)
for i, e in enumerate(l):
    if e: o -= 1
    else: z -= 1
    if z * o == 0:
        print(i + 1)
        return
