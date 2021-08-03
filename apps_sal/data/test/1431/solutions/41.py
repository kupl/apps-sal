n = int(input())
l = list(map(int, input().split()))
box = [0] * (n + 1)
for i in range(n):
    k = n - i
    count = 0
    for j in range(k, n + 1, k):
        count += box[j]
    if count % 2 != l[k - 1]:
        box[k] = 1
ll = []
for i in range(1, n + 1):
    if box[i] == 1:
        ll.append(i)
print(box.count(1))
print(*ll)
