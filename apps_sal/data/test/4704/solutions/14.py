n = int(input())
a = list(map(int, input().split()))
sa = sum(a)
cs = 0
arr = []
for i in range(n - 1):
    cs += a[i]
    ca = sa - cs
    arr.append(abs(cs - ca))
print(min(arr))
