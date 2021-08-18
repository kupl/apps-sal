a, b, c, d = map(int, input().split())


takahashi_hp = a
aoki_hp = c

while True:
    aoki_hp = aoki_hp - b
    if aoki_hp <= 0:
        print("Yes")
        break
    takahashi_hp = takahashi_hp - d
    if takahashi_hp <= 0:
        print("No")
        break
