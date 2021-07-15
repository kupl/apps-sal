nums = list(map(int, input().split()))
k = int(input())
x = max(nums)
mulx = x*(2**k)
print((mulx + sum(nums)-x))

