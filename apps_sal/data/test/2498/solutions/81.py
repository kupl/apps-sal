# 参考 : https://at274.hatenablog.com/entry/2020/01/15/060000
from functools import reduce
import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_list(numbers):  # リストを投げると全要素のlcmが返ってくる
    return reduce(lcm, numbers, 1)


N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

# 最初、Aの要素は全て偶数。2で割ったものに置き換え
A = [a // 2 for a in A]

# 全ての要素について、２で割れる回数が同じでないと題意は満たせない
count_div_2 = None
for a in A:
    cnt = 0
    while a % 2 == 0:
        a //= 2
        cnt += 1
    # 1個目は無条件で保存
    if count_div_2 is None:
        count_div_2 = cnt
    # 2個目からチェック
    elif cnt != count_div_2:
        print((0))
        return

# my_lcm = Aの全要素の最小公倍数。　この奇数倍が題意を満たす。
# my_lcmがMを超えていたら1つも作れない
my_lcm = lcm_list(A)
if my_lcm > M:
    print((0))
    return

tmp = M // my_lcm
# my_lcmの1,2,...M倍まで使えるが、偶数は使えない
# tmp=1or2なら1個, 3or4なら2個, 5or6なら3個,...
ans = (tmp + 1) // 2
print(ans)
