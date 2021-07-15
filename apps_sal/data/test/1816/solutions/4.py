n = int(input())
lst = list(map(int, input().split()))
d = []
for i in range(n):
    d.append((lst[i], i))
d.sort()    
s = 0
for i in range(1, n):
    s += abs(d[i][1] - d[i - 1][1])
print(s)    
    

