# 整数A,B AもBも割れる整数でK番目に大きいもの

A,B,K = map(int,input().split())

warerukazu = []

for i in range(1,101):
    if A % i == 0 and B % i == 0:
        warerukazu.append(i)

print(warerukazu[-K])
