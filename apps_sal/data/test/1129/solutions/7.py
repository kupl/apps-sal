n = int(input())
numbers = [int(n) for n in input().split()]
ns = sorted(numbers)
print(ns[(n - 1) // 2])
