import math
n = input()
arr = [int(i) for i in n]
n = int(arr[0]) * 10000 + int(arr[2]) * 1000 + int(arr[4]) * 100 + int(arr[3]) * 10 + int(arr[1])
n = n ** 5 % 100000
print('%05d' % n)
