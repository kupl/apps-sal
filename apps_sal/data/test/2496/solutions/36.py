

#素因数分解（10**6まで）
def soinsu_bunkai(m):
    pf=set()
    mm =m
    pri_num =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]
    for i in pri_num:
        if i > mm:
            break
        while mm %i==0:
            pf.add(i)
            mm //=i
    if mm !=1:
        pf.add(mm)
    return pf

# 初期入力
import math
import sys
from functools import reduce
input = sys.stdin.readline  #文字列では使わない
N = int(input())
A = list(map(int, input().split()))
used =set()
pair_w =set()

# 10**6までの素因数分解するために、「10**6のルート」までの素数を列挙
pri =10**6 +10

#not coprimeの判定
gcd_a =reduce(math.gcd,A)
if gcd_a !=1:
    ans ="not coprime"

#pairwise coprimeの判定
else:
    ans ="pairwise coprime"
    for a in A:
        aa =soinsu_bunkai(a)
        if used & aa:
            print("setwise coprime")
            return #共通要素があったらpair_wではない→set_w
        used |=aa

        
print(ans)
