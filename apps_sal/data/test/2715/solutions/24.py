import heapq
k = int(input())
a = [49] * 50
for i in range(50):
    a[i] += k // 50
k %= 50


for i in range(k):
    for j in range(50):
        if i == j: a[j] += k
        else: a[j] -= 1

print(len(a))
print(' '.join(list(map(str, a))))
