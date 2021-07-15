n = int(input())
a = [int(i) for i in input().split()]
b = {}
for i in range(n):
    b[a[i]] = i
b = sorted(b.items(), key=lambda x:x[1])
print(b[0][0])
