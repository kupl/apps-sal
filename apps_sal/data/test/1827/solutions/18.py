b = int(input())
a = [int(i) for i in input().split()]
c = 0
for i in range(len(a)) :
    c += a[i]
c /= b
while len(a) > 0 :
    d = a.pop(0)
    for i in range(len(a)) :
        if a[i] == c-d :
            f = a.pop(i)
            break
    print(d , f)
