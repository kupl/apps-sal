n = int(input())
a = list(map(int, input().split()))
x = max(a)
s = 0
for i in range(n):
    s += x - a[i]
print(s)
