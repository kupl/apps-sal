n = int(input())
p = list(map(int, input().split()))

used = [False] * n
nums = list()


def count(i):
    c = 0
    while True:
        if used[i]:
            return c
        else:
            used[i] = True
            i = p[i] - 1
            c += 1


for i in range(n):
    if not used[i]:
        nums.append(count(i))

if n == 1:
    print(1)
elif n == 2:
    print(4)
else:
    nums.sort(reverse=True)
    if len(nums) > 1:
        c = (nums[0] + nums[1]) ** 2
        for i in nums[2:]:
            c += i ** 2
        print(c)
    else:
        print(nums[0] ** 2)

