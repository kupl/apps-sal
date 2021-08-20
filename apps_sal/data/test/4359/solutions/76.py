menu = []
for i in range(5):
    menu.append(input())
mini = 10
a = 0
for i in range(5):
    m = int(menu[i][-1])
    if 1 <= m <= mini:
        mini = m
        a = i
menu = [int(s) for s in menu]
ans = 0
for i in range(5):
    if i == a:
        ans += menu[i]
    else:
        ans += -(-menu[i] // 10) * 10
print(ans)
