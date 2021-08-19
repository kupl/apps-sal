(N, K) = list(map(int, input().split()))
num_list = []
for i in range(2 * K):
    num_list.append(list(map(int, input().split())))
list1 = []
s = 0
while s < 2 * K - 1:
    list1.append(num_list[s + 1])
    s = s + 2
list2 = []
for i in range(K):
    x = len(list1[i])
    t = 0
    while t < x:
        list2.append(list1[i][t])
        t = t + 1
z = len(set(list2))
print(N - z)
