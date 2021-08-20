(n, k) = list(input().split())
res_n_i = 0
res = 0
for i in range(int(n)):
    n_i = input()
    for j in range(int(k) + 1):
        if str(j) in n_i:
            res_n_i += 1
        else:
            res_n_i = 0
            break
        if res_n_i == int(k) + 1:
            res += 1
            res_n_i = 0
print(res)
