n = int(input())
k = int(input())
nums = list(map(int, input().split()))
print(2 * sum([min(k - i, i) for i in nums]))
