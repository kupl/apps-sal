n, p = list(map(int, input().split()))
s = list(map(int, input().strip()))

count = 0

if(p == 2 or p == 5):  # 10と互いに素ではない場合
    co = 0
    for i in range(n):  # 1の位から順に数を追加していく
        ne = int(s[n - i - 1]) % p
        if(ne == 0):
            co += 1
        count += co
    print(count)
else:
    sta = [0] * p
    sta[0] += 1
    d = 1
    co = 0
    for i in range(n):
        ne = int(s[n - i - 1]) * d % p
        co += ne
        co %= p
        sta[co] += 1
        d *= 10
        d %= p
    for i in range(p):
        count += sta[i] * (sta[i] - 1) // 2
    print(count)
