s = input().split()
n = int(s[0])
c = int(s[1])
a = input().split()
k = 1
for i in range(n - 1):
    if int(a[i + 1]) - int(a[i]) <= c:
        k += 1
    else:
        k = 1

print(k)
