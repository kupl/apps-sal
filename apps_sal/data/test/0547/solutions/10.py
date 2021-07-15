n, k = map(int, input().split())
dat = [len(input()) for i in range(n)]
p = len(input())
mi = sum(map(lambda x: x < p, dat))
ma = mi + sum(map(lambda x: x == p, dat)) - 1

print(mi + (mi//k)*5 + 1, end = " ")
print(ma + (ma//k)*5 + 1)
