n = int(input())
lst = list(map(int,input().split()))
tmp = 0
for i in range(n):
  tmp = tmp + 1/lst[i]
print(1/tmp)
