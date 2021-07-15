add = 0
n = int(input())
mx = 0
arr = input().split(" ")
a = []
for elem in arr:
 a.append(int(elem))
for k in range(len(a)):
 if a[k] == 0:
  add = 0
 else:
  add += 1
 if add > mx:
  mx = add
print(mx)

