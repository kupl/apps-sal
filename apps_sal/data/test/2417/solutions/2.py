n = int(input())

arr1 = list(map(int, input().split(' ')))
arr2 = list(map(int, input().split(' ')))

excluded = [False] * (n + 1)
sol = 0

i = 0
j = 0

while(i < n and j < n):
  if(excluded[arr1[i]]):
    i += 1
    continue

  if(arr1[i] == arr2[j]):
    i += 1
    j += 1
  else:
    excluded[arr2[j]] = True
    j += 1
    sol += 1
  
print(sol)

