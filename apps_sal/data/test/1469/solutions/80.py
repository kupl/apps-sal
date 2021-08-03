def in_list(l, l_t, a):
    l[a] = l_t


ans_list = [[] for _ in range(60)]
p = 0

l = int(input())
bin_str = format(l, '020b')
for i in range(20):
    c = 0
    if c == 0 and str(bin_str)[i] == '1':
        c = 1
        n = 20 - i
        k = i
        break
for j in range(1, n):
    in_list(ans_list, [j, j + 1, 0], p)
    p += 1
    in_list(ans_list, [j, j + 1, 2**(n - 1 - j)], p)
    p += 1
c = 2**(n - 1)

for m in range(k + 1, 20):
    if str(bin_str[m]) == '1':
        in_list(ans_list, [1, n + m - 20 + 1, c], p)
        p += 1
        c += 2 ** (19 - m)

print(n, p)
for q in range(p):
    print(ans_list[q][0], ans_list[q][1], ans_list[q][2])
