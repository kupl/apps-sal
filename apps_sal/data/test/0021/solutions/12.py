n = int(input())
nums = [int(_) for _ in input().split()]

a = nums.index(1)
b = nums.index(n)
print(max(a, n - 1 - a, b, n - 1 - b))
