a = [int(i) for i in input().split()]
a_list = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and (k != i):
                a_list.append(abs(a[i] - a[j]) + abs(a[k] - a[i]))
print(min(a_list))
