A, B, C = map(lambda x: int(x), input().split())
SA = ((A + 1) * A // 2) % 998244353
SB = ((B + 1) * B // 2) % 998244353
SC = ((C + 1) * C // 2) % 998244353

print((SA * SB * SC) % 998244353)
