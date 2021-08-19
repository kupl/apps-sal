n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
tmp1 = tmp2 = 0
for i in range(n):
    tmp1 |= a[i]
    tmp2 |= b[i]
print(tmp1 + tmp2)
