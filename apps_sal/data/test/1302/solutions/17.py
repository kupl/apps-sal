n, k = map(int, input().split())
# n - 1 with gcd > 1 because any number gcd with itself is > 1
array = [0] + [i+1 for i in range(n)]
# print(*array[1:])
if n == k:
    print(-1)
else:
    for i in range(0, n-k-1):
    	# All consecutive numbers are coprimes, every swap removes a coprime
        array[1], array[n-i] = array[n-i],array[1]
        # print(*array[1:])
    print(*array[1:])
