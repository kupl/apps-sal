(n, c) = list(map(int, input().split()))
x_list = []
v_list = []
one_list = []
round_list = []
r_one_list = []
r_round_list = []
total = 0
for i in range(n):
    (x, v) = list(map(int, input().split()))
    x_list.append(x)
    v_list.append(v)
    total = total + v
    one_list.append(total - x)
    round_list.append(total - 2 * x)
prev = 0
for i in range(n):
    if prev > one_list[i]:
        one_list[i] = prev
    else:
        prev = one_list[i]
prev = 0
for i in range(n):
    if prev > round_list[i]:
        round_list[i] = prev
    else:
        prev = round_list[i]
total = 0
for i in range(1, n + 1):
    total = total + v_list[-i]
    r_one_list.append(total - (c - x_list[-i]))
    r_round_list.append(total - 2 * (c - x_list[-i]))
prev = 0
for i in range(n):
    if prev > r_one_list[i]:
        r_one_list[i] = prev
    else:
        prev = r_one_list[i]
prev = 0
for i in range(n):
    if prev > r_round_list[i]:
        r_round_list[i] = prev
    else:
        prev = r_round_list[i]
ret = 0
for i in range(n - 1):
    tmp = max(one_list[i] + r_round_list[-i - 2], round_list[i] + r_one_list[-i - 2])
    if tmp > ret:
        ret = tmp
ret = max(one_list[-1], r_one_list[-1], ret)
print(ret)
