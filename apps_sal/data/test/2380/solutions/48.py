N, M = map(int, input().split())
A_list = sorted(list(map(int, input().split())))
BC_list = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[1], reverse=True)
change_list_sorted = []
for m in range(M):
    b, c = BC_list[m]
    for _ in range(b):
        change_list_sorted.append(c)
    if len(change_list_sorted) > N:
        break
change_cnt = 0
for i, (change_val, a) in enumerate(zip(change_list_sorted, A_list)):
    if a <= change_val:
        A_list[i] = change_val
    else:
        break
print(sum(A_list))
