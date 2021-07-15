lst = input().split()

for i in range(3):
   lst[i] = int(lst[i])

lst.sort()
print(lst[0] + lst[1])
