from functools import reduce
n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
(a, b) = (reduce(lambda x, y: x | y, A), reduce(lambda x, y: x | y, B))
print(a + b)
