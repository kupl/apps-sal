n = int(input())
sosuu = [2]
A = 1000
for L in range(3, A, 2):
    for L2 in sosuu:
        if L % L2 == 0:
            break
    else:
        sosuu.append(L)
ans = []
for i in sosuu:
    ch = 1
    x = i
    while x <= n:
        ch += n // x
        x = x * i
    ans.append(ch)
ans1 = 1
mod = 10 ** 9 + 7
for j in ans:
    ans1 = ans1 * j % mod
print(ans1)
