# 入力を受け通る
N=int(input())
A=list(map(int,input().split()))

# 逆数の総和を求める
tmp=0
for a in A:
    tmp += 1/a

# 総和の逆数を求める
ret=1/tmp

print(ret)
