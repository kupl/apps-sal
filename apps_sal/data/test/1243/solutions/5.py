n = int(input())
a = list(map(int, input().split()))
k = sum(a)
s = 0
r = 0
for i in range(n):
    s += k // n - a[i]
    r += abs(s)
print(r)
