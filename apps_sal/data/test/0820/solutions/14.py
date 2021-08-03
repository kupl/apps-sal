n = int(input())
m = int(input())
l = []
for i in range(n):
    l.append(int(input()))

l.sort()
k = 0
r = 0
i = n - 1
while(i >= 0):
    k += l[i]
    r += 1
    if(k >= m):
        break
    i -= 1

print(r)
