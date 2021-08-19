inp = input().split()
n = int(inp[0])
k = int(inp[1])
a = input().split()
b = []
x = 0
temp = []

for i in a:
    temp = []
    x = int(i)
    if x == 100:
        temp.append(0)
        temp.append(x)
    else:
        temp.append(10 - x % 10)
        temp.append(x)
    b.append(temp)
# print(b)
b.sort()
# print(b)
j = 0
ss = 0
c = []
for t in b:
    if t[0] == 0:
        pass
    elif (t[0] <= k) and (k != 0):
        k -= t[0]
        t[1] += t[0]
        t[0] = 0
    c.append(t[1] // 10)
c.sort()
j = 0
k = k // 10
#print(c, k)
while j < n:
    #print(c[j], k)
    if ((10 - c[j]) <= k):
        k -= (10 - c[j])
        c[j] = 10
    else:
        c[j] += k
        k = 0
    ss += c[j]
    j += 1
# print(c)
print(ss)
