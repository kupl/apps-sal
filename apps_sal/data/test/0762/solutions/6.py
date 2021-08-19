(n, m) = list(map(int, input().split()))
ls = [int(i) for i in input().split()]
(odd_num, even_num) = (0, 0)
cur_odd = 0
cur_even = 0
ans = []
for i in range(n - 2):
    if ls[i] & 1:
        cur_odd += 1
    else:
        cur_even += 1
    if i >= 1 and cur_odd == cur_even:
        ans.append(abs(ls[i + 1] - ls[i]))
ans.sort()
res = 0
for i in ans:
    if m - i >= 0:
        m -= i
        res += 1
    else:
        break
print(res)
