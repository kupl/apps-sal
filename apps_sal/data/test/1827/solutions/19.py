n = int(input())
a = input().split()
s = 0
for i in range(len(a)):
    a[i] = int(a[i])
    s = s + a[i]
l = s//n
a.sort()

for i in range(n):
    print(a[i],l-a[i])

