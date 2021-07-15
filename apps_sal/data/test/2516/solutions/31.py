'''ika tako　　ABC164Dの類題
基本は、1桁目、2桁目と下から10進数の数字として見て、
素数ｐで割った余りを考え、余りが同じである数字のスタートとエンドを
選ぶ組み合わせの数が答。
但し、10進数で考えているので、ｐが2と5のケースは別扱い。
末尾が2、5の倍数なら2の倍数。先頭の数字を0番目として、
i番目に2、5の倍数が出てきたら、
そこを右端とする部分文字列は i+1  個作れる。
'''
from collections import defaultdict

def solve2(s):
    ans = 0
    for i, c in enumerate(s):
        if c in '02468':
            ans += i + 1
    return ans

def solve5(s):
    ans = 0
    for i, c in enumerate(s):
        if c in '05':
            ans += i + 1
    return ans

def solve_other(s, p):
    reminders = defaultdict(lambda: 0)
    tmp = 0
    mul = 1
    for c in s[::-1]:
        c = int(c)
        tmp = (tmp + c * mul) % p
        mul = mul * 10 % p
        reminders[tmp] += 1
    reminders[0] += 1
    ans = 0
    for r, cnt in reminders.items():
        ans += cnt * (cnt - 1) // 2
    return ans

n, p = list(map(int, input().split()))
s = input()
if p == 2:
    print(solve2(s))
elif p == 5:
    print(solve5(s))
else:
    print(solve_other(s, p))
