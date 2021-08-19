(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if k % a[i] == 0:
        b.append(a[i])
print(k // max(b))
