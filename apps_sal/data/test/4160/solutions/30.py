X = int(input())
ii = 0
k = 100
while k < X :
    ii += 1
    k += k//100
print(ii)
