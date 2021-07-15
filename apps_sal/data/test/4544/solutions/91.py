n = int(input())
a_lst = list(map(int, input().split()))
for i in range(n):
    a_lst[i] += 1

max_a = max(a_lst)
count_lst = [0] * (max_a + 2)


for i in range(n):
    a = a_lst[i]
    index1 = a - 1
    index2 = a
    index3 = a + 1

    count_lst[index1] += 1
    count_lst[index2] += 1
    count_lst[index3] += 1

maximum = max(count_lst)
print(maximum)
