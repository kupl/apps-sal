def main(n, nums):
    data = {}
    Rn = range(n)
    answer = 0
    for i in Rn:
        item = str(nums[i])
        if item != '0':
            if item not in data:
                data[item] = 0
            data[item] += 1
    for item in data.keys():
        val = data[item]
        if val == 2:
            answer += 1
        elif val > 2:
            return -1
    return answer


def init():
    n = int(input())
    nums = list(map(int, input().split()))
    print(main(n, nums))


init()
