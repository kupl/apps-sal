N = int(input())
a = list(map(int, input().split()))
a.sort()

k = 1
while True:
  for i in range(len(a)):
    if a[i] < (i//k):
      break
  else:
    print(k)
    break
  k += 1
