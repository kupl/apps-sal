a, b, c, d = map(int, input().split())

# 高橋君のモンスターは体力が A で攻撃力が B です。  a-d
# 青木君のモンスターは体力が C で攻撃力が D です。  c-b

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
