(n, x) = map(int, input().split())
data = list(map(int, input().split()))
k = 0
for i in range(x):
    if i not in data:
        k += 1
if x in data:
    k += 1
print(k)
