n = int(input())
l = list(map(int, input().strip().split()))
m = []
cur = 1
last = l[0]
for i in range(1,n):
    if l[i] != last:
        m.append(cur)
        cur = 1
        last = l[i]
    else:
        cur += 1
m.append(cur)
mx = 0
for i in range(len(m) - 1):
    mx = max(mx,min(m[i],m[i+1]))
print(mx*2)

