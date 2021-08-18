A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
MENU = [A, B, C, D, E]

amari = 0
amari_mod = 10
ans = 0
amari_cnt = 0

for menu in MENU:
    if menu % 10 < amari_mod and menu % 10 != 0:
        amari = menu
        amari_mod = menu % 10

for menu in MENU:
    if menu == amari and amari_cnt == 0:
        ans += menu
        amari_cnt += 1
    elif menu % 10 == 0:
        ans += menu
    else:
        menu = menu - menu % 10 + 10
        ans += menu

print(ans)
