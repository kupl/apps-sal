"""
上のほうが餅が小さくなるように重ねる
→ 同じサイズの餅は使えない

同じサイズの餅は1つだけ使って（重複を排除して）
大きいものから重ねていけばいい

何段重ねられるか
= 何種類のサイズの餅があるか
"""
n = int(input())
mochi_set = set()
for i in range(n):
    size = int(input())
    mochi_set.add(size)
print(len(mochi_set))
