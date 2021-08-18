s = input()
x, y = list(map(int, input().split()))

n = len(s)

temp = 0
xys = [[], []]

xy = 0

first = True


for i in range(n):
    if(s[i] == 'F'):
        temp += 1
    else:
        if(temp != 0):
            if(first):
                x -= temp
            else:
                xys[xy].append(temp)
            temp = 0
        xy = (xy + 1) % 2
        first = False

if(temp != 0):
    if(first):
        x -= temp
    else:
        xys[xy].append(temp)
        temp = 0

for xy, target in zip([0, 1], [x, y]):
    nums = xys[xy]
    len_ = len(nums)

    if(len_ == 0):
        if(target == 0):
            continue
        else:
            print('No')
            return

    target = abs(target)
    sum_ = sum(nums)

    if((sum_ - target) % 2 == 1) | (target > sum_):
        print('No')
        return

    max = 1 + (sum_ - target) // 2

    dp = [[0] * max for _ in range(len_ + 1)]
    dp[0][0] = 1

    for i in range(1, len_ + 1):
        dp[i][0] = 1
        temp = nums[i - 1]
        for j in range(temp, max):
            dp[i][j] = dp[i - 1][j - temp] | dp[i - 1][j]

        if(dp[i][-1] == 1):
            break

        if(i == len_):
            print('No')
            return


print('Yes')
