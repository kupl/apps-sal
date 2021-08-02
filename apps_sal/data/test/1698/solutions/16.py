n, k = list(map(int, input().split()))
c = 0
a = list(map(int, input().split()))
a.sort()
while(a):
    t = []
    for i in range(k):
        if(a):
            t.append(a.pop())
    c += (max(t) - 1) * 2
    t.clear()
print(c)
