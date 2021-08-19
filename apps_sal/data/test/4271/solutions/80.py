n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
res = b[a[0] - 1]
for i in range(1, n):
    # print(i,res,a[i])
    res += b[a[i] - 1]
    if a[i - 1] + 1 == a[i]:
        res += c[a[i - 1] - 1]
print(res)
