(a, b, k) = [int(x) for x in input().split()]
(a_list, b_list) = ([], [])
for ai in range(1, a + 1):
    if a % ai == 0:
        a_list.append(ai)
for bi in range(1, b + 1):
    if b % bi == 0:
        b_list.append(bi)
list_ = [b for b in b_list if b in a_list]
print(list_[-k])
