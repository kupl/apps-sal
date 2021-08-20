(n, k) = list(map(int, input().split()))
ans = []
count = 0
for i in range(n):
    a = list(map(int, input().split()))
    if min(a[1:]) < k:
        count += 1
        ans.append(i + 1)
print(count)
if count > 0:
    sep = ' '
    print(sep.join(list(map(str, ans))))
