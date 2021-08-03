n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a.sort()
s = 0
k = 0
for i in a:
    if i >= s:
        k += 1
        s = s + i
print(k)
