def seq1(diff, nums):
    index = diff[0][1]
    a, b = nums[index][0], nums[index][1]
    if b > a:
        indices = [index]
    else:
        return []
    x1, x2 = a, b
    for i in range(1, len(diff)):
        index = diff[i][1]
        a, b = nums[index][0], nums[index][1]
        if x2 > a and a < b:
            indices.append(index)
            x2 = b
        else:
            break

    return indices


def seq2(diff, nums):
    index = diff[0][1]
    a, b = nums[index][0], nums[index][1]
    if b < a:
        indices = [index]
    else:
        return []
    x1, x2 = a, b
    for i in range(1, len(diff)):
        index = diff[i][1]
        a, b = nums[index][0], nums[index][1]
        if a > x2 and a > b:
            indices.append(index)
            x2 = b
        else:
            break

    return indices


def main():
    n = int(input())
    nums = []
    diff1 = []
    diff2 = []
    for i in range(n):
        a, b = map(int, input().split())
        nums.append((a, b))
        if b - a > 0:
            diff1.append((b, i))
        else:
            diff2.append((a, i))

    diff1.sort(reverse=True)
    diff2.sort()
    if diff1:
        ans1 = seq1(diff1, nums)
    else:
        ans1 = []
    if diff2:
        ans2 = seq2(diff2, nums)
    else:
        ans2 = []

    if len(ans1) >= len(ans2):
        print(len(ans1))
        for i in ans1:
            print(i + 1, end=' ')
    else:
        print(len(ans2))
        for i in ans2:
            print(i + 1, end=' ')


main()
