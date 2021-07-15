n = int(input())
numbers =  [int(x) - 100 for x in input().split()]

maxi = 0
acc_index = -1

for acc_index in range(n):
  suma = 0
  for index in range(acc_index, n):
    suma = suma + numbers[index]
    if suma > 0:
      maxi = max(maxi, index-acc_index+1) 

print(maxi) 
