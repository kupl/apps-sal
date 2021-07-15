K = int(input())
R = 0
for i in range(1, K + 10):
  R *= 10
  R += 7
  R %= K
  if R == 0:
    print(i)
    import sys
    return
print((-1))

