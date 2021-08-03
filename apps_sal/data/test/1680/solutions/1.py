from collections import defaultdict
n, k = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

A_dict = defaultdict(int)
for i in A:
    A_dict[i] += 1


def bitCount(x):
    cur = 0
    while x > 0:
        if x % 2:
            cur += 1
        x //= 2
    return cur


mask = []
for i in range(2**15):
    if bitCount(i) == k:
        mask.append(i)


ans = 0
for i in A_dict:
    for j in mask:
        if i ^ j in A_dict:
            if i ^ j == i:
                ans += A_dict[i] * (A_dict[i] - 1)
            else:
                ans += A_dict[i] * A_dict[i ^ j]
print(ans // 2)
