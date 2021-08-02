n, k = input().strip().split(' ')
n, k = (int(n), int(k))
list1 = list(map(int, input().strip().split(' ')))
ls = [x for x in range(1, n * k + 1)]
for i in range(k):
    ls.remove(list1[i])
list2 = []
i = 0
j = 0
while j < k:
    print(*(ls[i:i + n - 1] + [list1[j]]))
    i += (n - 1)
    j += 1
