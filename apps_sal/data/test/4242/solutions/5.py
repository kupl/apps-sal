A, B, K = map(int, input().split())

# AもBも割り切る正整数のうち、K番目に大きいものを出力せよ。

count = []
c = min(A, B)
for i in range(1, c + 1):
  if (A % i == 0) and (B % i == 0):
    count.append(i)
print(count[-K])
