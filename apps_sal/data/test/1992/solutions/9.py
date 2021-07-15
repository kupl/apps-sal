n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = {}
for i in range(len(a)):
    d[a[i]] = i
cnt = 0
for i in range(len(b)):
    cnt += ((d[b[i]]) // k)
    cnt += 1
    if d[b[i]] != 0:
        d[b[i]] -= 1
        d[a[d[b[i]]]] += 1
        m = a[d[b[i]]]
        a[d[b[i]]] = a[d[b[i]] + 1]
        a[d[b[i]] + 1] = m 
    
print(cnt)
    
    
    

