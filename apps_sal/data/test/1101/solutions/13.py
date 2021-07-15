res = 1e9
def next(i):
    i+=1
    while(i < n and s[i] == '1'):
        i+=1
    return i

n,k = list(map(int, input().split()))
s = input()
l = next(-1)
m = l
r = l
for i in range(k):
    r = next(r)
  
while(r < n):
    while(max(m - l, r - m) > max(next(m) - l, r - next(m))):
        m = next(m)
    res = min(res, max(m - l, r - m))
    l = next(l)
    r = next(r)
print(res)

