sa = int(input())
array = [0] + list(map(int, input().split(' ')))
array2 = [array[x] - array[x + 1] for x in range(len(array) - 1)]
maxx = 0
drop = pow(10, 19)
for element in array2:
    maxx += element
    if maxx < drop:
        drop = maxx
print(abs(drop))
