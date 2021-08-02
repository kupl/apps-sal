n = int(input())
a = [int(input()) for i in range(n)]
sa = sorted(a)

for i in a:
    if sa[-1] == i:
        print(sa[-2])
    else:
        print(sa[-1])
