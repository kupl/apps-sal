n = int(input())
s = 0
h = 0
for i in range(n):
    res = input().strip().split()[-1]
    if res == 'soft':
        s+=1
    else:
        h+=1

b, w = min (s,h), max(s,h)
for k in range(n):
    if ((k**2) //2) >= b and ((k**2) - ((k**2)//2))>= w:
        print(k)
        return
print(n)

