k = int(input())

# 関数S(n)


def S(num):
    s = sum(map(int, list(str(num))))
    return num / s


# 1~9と 〇9-> 〇99 -> 〇999 を出力
ten = 0
now = 1
# k回ループ
for _ in range(k):
    print(now)
    # 桁が変わる時にten+=1する
    if S(now + 10**ten) > S(now + 10**(ten + 1)):
        #print(now,S(now + 10**ten), S(now + 10**(ten + 1)))
        ten += 1
    now += 10**ten
