# 最小公倍数(mathは3.5以降) 
 #参考　https://note.nkmk.me/python-gcd-lcm/
from functools import reduce
import math #(2020-0405  fractions→math)
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y) # 「//」はフロートにせずにintにする
def lcm(*numbers): # a,b,cなど
    return reduce(lcm_base, numbers, 1)
def lcm_list(numbers): #リスト
    return reduce(lcm_base, numbers, 1)


# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
N = int(input())
a = list(map(int, input().split()))

saisyo_koubaisu =lcm_list(a)
ans =0
for aa in a:
    ans += (saisyo_koubaisu-1) %aa
print(ans)
