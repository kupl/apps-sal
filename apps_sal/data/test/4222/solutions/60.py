n, k = list(map(int, input().split()))

s = []

for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for i in range(d):
        s.append(a[i])
        
t = sorted(s)
a = len(t)
x = n

for i in range(n):
    for k in range(a):
        if i + 1 == t[k]:
            x -= 1
            break
        elif i + 1 < t[k]:
            break
        
print(x)

