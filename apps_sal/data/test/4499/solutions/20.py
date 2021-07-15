a = input().split()
res = ""
for i in range(len(a)):
    a[i] = a[i].upper()
    res += a[i][0]
print(res)
