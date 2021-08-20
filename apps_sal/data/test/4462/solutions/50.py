n = int(input())
a_ls = list(map(int, input().split()))
n_4k = 0
n_2k = 0
n_odd = 0
for i in range(n):
    if a_ls[i] % 4 == 0:
        n_4k += 1
    elif a_ls[i] % 2 == 0:
        n_2k += 1
    else:
        n_odd += 1
res = 'No'
if n_odd == 0:
    res = 'Yes'
elif n_2k > 0:
    if n_odd <= n_4k:
        res = 'Yes'
elif n_odd <= n_4k + 1:
    res = 'Yes'
print(res)
