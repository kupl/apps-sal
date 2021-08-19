cnt = int(input())
hp = 0
if cnt >= 500:
    hp += 1000 * (cnt // 500)
    cnt %= 500
hp += 5 * (cnt // 5)
print(hp)
