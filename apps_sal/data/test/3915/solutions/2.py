n = 12 * 10 ** 5
(p, q) = map(int, input().split())
pr = [0] * n
pr[1] = 1
for i in range(2, n):
    if pr[i] == 1:
        continue
    for j in range(2 * i, n, i):
        pr[j] = 1
res = 'Palindromic tree is better than splay tree'
rub = pi = 0
for i in range(1, n):
    if pr[i] == 0:
        pi += 1
    if str(i) == str(i)[::-1]:
        rub += 1
    if pi * q <= rub * p:
        res = i
print(res)
