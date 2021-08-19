n = int(input())
a = [int(input()) for _ in range(n)]
maxa = max(a)
maxnum = a.count(maxa)
if maxnum > 1:
    for i in range(n):
        print(maxa)
else:
    maxidx = a.index(maxa)
    for i in range(n):
        if i != maxidx:
            print(maxa)
        else:
            a[maxidx] = 0
            print(max(a))
