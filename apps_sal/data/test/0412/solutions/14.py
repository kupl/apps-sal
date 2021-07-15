n = int(input())
a = [0]*n
s = input().split()
x = 0
y = 0
b = []
for i in range(n):
    a[i] = int(s[i])
for i in range(n):
    while (a[i])%2==0:
        a[i]=(a[i]//2)
        x += 1
    b.append(x)
    x = 0
print(2**(max(b)), b.count(max(b)))


