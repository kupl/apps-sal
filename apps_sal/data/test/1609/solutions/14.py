n = int(input())
lst = list(map(int, input().split()))
mn = set()
ans = set()
sp = []
for i in range(1, n + 1):
    mn.add(i)
for i in lst:
    if i in mn:
        mn.remove(i)
for i in lst:
    if i in ans or i > n:
        a = mn.pop()
        ans.add(a)
        sp.append(a)
    if i not in ans and i <= n:
        ans.add(i)
        sp.append(i)
    
print(*sp)    

