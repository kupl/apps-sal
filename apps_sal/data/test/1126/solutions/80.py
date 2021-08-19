(n, x, m) = map(int, input().split())
check = [False] * (10 ** 5 + 10)
check_list = [x]
a = x
for i in range(n):
    a = a * a % m
    if check[a]:
        break
    check[a] = True
    check_list.append(a)
index = check_list.index(a)
loop_bef = check_list[0:index]
loop = check_list[index:]
loop_num = (n - len(loop_bef)) // len(loop)
after_loop = (n - len(loop_bef)) % len(loop)
ans = sum(loop_bef) + sum(loop) * loop_num + sum(loop[:after_loop])
print(ans)
