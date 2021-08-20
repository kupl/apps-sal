s = input()[::-1]
p = 2019
ans = [0] * p
(x10, S) = (1, 0)
for i in s:
    S += x10 * int(i)
    S %= p
    x10 *= 10
    x10 %= p
    ans[S] += 1
cnt = ans[0]
for a in ans:
    cnt += a * (a - 1) // 2
print(cnt)
