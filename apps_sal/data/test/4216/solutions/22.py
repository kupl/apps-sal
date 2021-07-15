N = int(input())
high_divs = []
k = 1

while k*k <= N:
  if N%k == 0:
    high_divs.insert(0,N//k)
  k += 1

print(len(str(high_divs[0])))
