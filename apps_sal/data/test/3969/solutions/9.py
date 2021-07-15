n, m = [int(x) for x in input().split()]
d = [0 for i in range(m)]
for i in range(n):
    c, x = [x for x in input().split()]
    c = int(c)

    d[c-1] = max(d[:c])+1
print(n-max(d))
        

