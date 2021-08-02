h, w = [int(ele) for ele in input().split(" ")]
MODULO = 998244353

print(2**(h + w) % MODULO)
