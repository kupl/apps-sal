n = int(input())
nums = list(map(int, input().split()))
re_nums = [1 / num for num in nums]
print(1 / sum(re_nums))
