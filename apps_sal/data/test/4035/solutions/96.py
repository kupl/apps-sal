a, b = map(int, input().split())

a_min = int(a / 0.08)
b_min = int(b / 0.1)
a_list = [i for i in range(a_min, a_min + 100, 1) if int(i * 0.08) == a]
b_list = [j for j in range(b_min, b_min + 100, 1) if int(j * 0.1) == b]

ans = -1
for k in a_list:
    if k in b_list:
        ans = k
        break

print(ans)
