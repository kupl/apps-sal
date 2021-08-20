(n, K) = [int(i) for i in input().split()]
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a.sort()
i = 0
j = 1
ans = n
while True:
    if j == n:
        break
    if a[j] == a[i]:
        j += 1
    elif a[i] + K >= a[j]:
        ans -= 1
        i += 1
    else:
        i += 1
print(ans)
