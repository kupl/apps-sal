N = int(input())
for i in range(11):
  if 1000*i - N >= 0:
    print(1000*i - N)
    break
