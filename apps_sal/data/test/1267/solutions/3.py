n = int(input())
a = list(set(map(int, input().split())))
a.sort()
if a[0] == 0:
    print(len(a) - 1)
else:
    print(len(a))
