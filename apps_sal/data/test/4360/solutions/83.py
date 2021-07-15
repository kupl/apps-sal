a = int(input())
b = list(map(int,input().split()))
c = 0
for i in range(a):
  c += 1/b[i]
print(1/c)
