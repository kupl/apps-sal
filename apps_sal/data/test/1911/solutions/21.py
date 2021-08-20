(n, k) = list(map(int, input().split()))
l = list(map(int, input().split()))
l1 = []
for i in range(n - 1):
    l1.append(l[i + 1] - l[i])
l1.sort()
if k == 1:
    print(sum(l1))
else:
    print(sum(l1[:-k + 1]))
