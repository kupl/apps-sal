# 38
menu = []
jissai_menu = []
for i in range(5):
    menu.append(int(input()))
    if menu[i] % 10 == 0:
        jissai_menu.append(menu[i])
    else:
        jissai_menu.append(menu[i] - menu[i] % 10 + 10)

ans = float('inf')
for i in range(5):
    tmp = 0
    for j in range(5):
        if j == i: continue
        tmp += jissai_menu[j]
    ans = min(ans, tmp + menu[i])

print(ans)
