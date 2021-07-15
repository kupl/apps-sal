n = int(input())
list_a = [int(i) for i in input().split()]
list_b = [int(j) for j in input().split()]
list_c = [int(k) for k in input().split()]
satisfied = 0
for i in range(0, len(list_a)):
    satisfied += list_b[list_a[i] - 1]
    if i > 0 and list_a[i] == list_a[i - 1] + 1:
        satisfied += list_c[list_a[i - 1] - 1]
print(satisfied)
