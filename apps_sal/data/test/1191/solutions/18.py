import array

n, k = list(map(int, input().split()))
p = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
s = []
for i in range(n):
    s.append((i, p[i], c[i]))
s = sorted(s, key=lambda x: x[1])
sum_list = [[s[0][2]]]
sum_res = [s[0][2]]
for i in range(1, n):
    sum_list.append(list(sum_list[i-1]))
    if i-k-1 >= 0:
        sum_list[i].remove(min(sum_list[i]))
    sum_list[i].append(s[i][2])
    sum_res.append(sum(sum_list[i]))

ans = [str(x[1]) for x in sorted(enumerate(sum_res), key=lambda x: s[x[0]][0])]

print(" ".join(ans))

