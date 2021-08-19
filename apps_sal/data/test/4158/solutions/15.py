n = int(input())
nums = list(map(int, input().split(' ')))
nums = sorted(nums)
power = [2 ** i for i in range(33)]


def search(x):
    low = 0
    high = len(nums)
    while low < high - 1:
        mid = (low + high) // 2
        if x > nums[mid]:
            low = mid
        elif x < nums[mid]:
            high = mid
        elif x == nums[mid]:
            return x
    return None


best = []
for i in power:
    for j in nums:
        result = []
        result.append(j)
        if search(j + i) is not None:
            result.append(j + i)
        if search(j + 2 * i) is not None:
            result.append(j + 2 * i)
        if len(result) > len(best):
            best = result
print(len(best))
print(' '.join(map(str, best)))
