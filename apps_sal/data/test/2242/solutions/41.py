S = input()
s_rev = S[::-1]
r_list = [0] * 2019
r_list[0] = 1
(num, d) = (0, 1)
for i in range(len(S)):
    num += d * int(s_rev[i])
    num %= 2019
    r_list[num] += 1
    d *= 10
    d %= 2019
ans = 0
for i in range(2019):
    ans += r_list[i] * (r_list[i] - 1) // 2
print(ans)
