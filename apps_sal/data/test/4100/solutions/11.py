n, k, q = list(map(int, input().split()))
a = []
count = []
for i in range(q):
    a.append(int(input()))
for i in range(n):
    count.append(0)

for i in range(q):
    count[a[i] - 1] += 1

for i in range(n):
    if k - q + count[i] <= 0:
        print("No")
    else:
        print("Yes")
