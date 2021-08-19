n = int(input())
a = [int(x.strip()) for x in input().split()]
ch, ans = 0, 0
flg = 'OK'
while flg == 'OK':
    for x in a:
        if x % 2 == 0:
            ch += 1
        else:
            break
    if ch == n:
        flg = 'OK'
        ch = 0
        ans += 1
        a = list(map(lambda x: int(x / 2), a))  # list関数にネストしないとmapオブジェクトでNGになる
    else:
        flg = 'NG'
print(ans)
