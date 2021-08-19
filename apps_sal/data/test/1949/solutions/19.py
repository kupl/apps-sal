def I():
    return list(map(int, input().split()))


(n, k) = list(map(int, input().split()))
a = list(set(I()))
a.sort()
s = 0
ind = 0
for i in range(k):
    if a:
        try:
            print(a[ind] - s)
            s += a[ind] - s
            ind += 1
        except:
            print(0)
    else:
        print(0)
