n, m = list(map(int, input().split()))
lst = [[int(x) for x in input().split()] for _ in range(m)]

tmp_lst = []

for row in lst:

    tmp_lst.append(row.index(max(row)))

tmp_tmp_lst = [0] * (n + 7)

for x in tmp_lst:
    tmp_tmp_lst[x] += 1


print(tmp_tmp_lst.index(max(tmp_tmp_lst)) + 1)
