n, m, k = [int(s) for s in input().split()]
array = [int(s) for s in input().split()]
array = sorted(array, reverse=True)
first = array[0]
second = array[1]
# print(array)
res = (first * k + second) * (m // (k + 1)) + first * (m % (k + 1))
print(res)
