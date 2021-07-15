n, k = map(int, input().split())
a = list(map(int, input().split()))
rec1, rec2 = [], []
num = 0
for i in range(n):
    if num == k:
        break
    if a[i] not in rec1:
        rec1.append(a[i])
        rec2.append(i + 1)
        num += 1

if num >= k:
    print("YES")
    print(" ".join(map(str, rec2)))
else:
    print("NO")
