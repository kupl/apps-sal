i = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
res = sum(b)
for j in range(i - 1):
    if a[j] + 1 == a[j + 1]:
        res += c[a[j] - 1]
print(res)
