k, n = map(int, input().split())
a = list(map(int,input().split()))
tmp = 0
ansl = [] 
for i in range(n-1):
    tmp = a[i+1] - a[i]
    ansl.append(tmp)
tmp = k - a[-1] + a[0]
ansl.append(tmp)
print(k -max(ansl))
