#約数
def make_divisors(n): #約数をリストで返す
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
N,M = (int(i) for i in input().split())
M_div =make_divisors(M)
div_rev =M_div[::-1]

#M=約数✖（相手）⇒相手＝n(n+1)/2 以上なら成り立つ
for i in range(len(M_div)):
    if N <= M_div[i]:
        print(div_rev[i])

        break 
