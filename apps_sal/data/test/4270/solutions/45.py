_ = input()
v = list(map(int,input().split()))
v.sort()
num = v[0]
for i in v:
  num = (num+i)/2
print(num)
