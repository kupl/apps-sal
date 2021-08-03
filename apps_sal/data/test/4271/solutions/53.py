n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = sum(b)
for i in range(n - 1):
    if a[i] - a[i + 1] == -1:
        d = d + c[a[i] - 1]
print(d)
