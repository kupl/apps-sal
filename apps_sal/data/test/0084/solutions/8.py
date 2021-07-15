n = int(input())
largest = n + n - 1
possible = [0, 9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 999999999]
maximum9 = 0
indx1 = 0
i = 0
for p in possible:
  if p <= largest and p > maximum9:
    maximum9 = p
    indx1 = i
  i += 1
indx2 = 0
for i in range(9):
  if largest >= i*10**indx1+maximum9:
    indx2 = i
  else:
    break
count = 0
for i in range(indx2+1):
  count += max((2*min(n, i*10**indx1+maximum9-1)- max(1,i*10**indx1+maximum9)+1)//2, 0)
print(count)

