n = int(input())
nums = list(map(int, input().split()))


def cost(x, y):
    return (x - y)**2


avg = round(sum(nums) / len(nums))

res = 0
for n in nums:
    res += cost(n, avg)
print(res)
