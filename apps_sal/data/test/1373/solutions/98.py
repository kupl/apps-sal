import math
(N, K) = list(map(int, input().split()))
list1 = list(range(N + 1))
list2 = []
for i in range(K, N + 2):
    min = math.floor(i * (list1[0] + list1[i - 1]) / 2)
    max = math.floor(i * (list1[N - i + 1] + list1[N]) / 2)
    list2.append(max - min + 1)
print(sum(list2) % (10 ** 9 + 7))
