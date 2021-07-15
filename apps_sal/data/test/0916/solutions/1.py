n= int(input())
a = [int(_) for _ in input().split()]
c = [int(_) for _ in input().split()]
depth = [0] * (n)
for i in range(1,n):
  depth[i] = depth[c[i-1]-1] + 1
MAX = max(depth)
t = 0
store = {}
todo = []
p = 0

for i in range(n):
    if (MAX-depth[i]) % 2 == 0: # odd, useful
        t ^= a[i]
        todo.append(a[i])
    else:
        store[a[i]]  = store.get(a[i],0) + 1
        p += 1

ans = 0
for i in todo:
    ans += store.get(i^t,0)

if t == 0:
    ans += (p*(p-1)//2) + (n-p)*(n-p-1)//2

print(ans)
