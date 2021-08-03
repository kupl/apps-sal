def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


n, m = getList()
nums = getList()


def solve(nums, m, i):
    tgt = nums[i]
    queue = nums[:i]
    queue.sort()
    for idx, q in enumerate(queue):
        tgt += q
        if tgt > m:
            return i - idx

    return 0


answers = []

for i in range(n):
    answers.append(solve(nums, m, i))


print(" ".join(list(map(str, answers))))
