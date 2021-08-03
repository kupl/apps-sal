import sys
lines = sys.stdin.readlines()
T = int(lines[0].strip())
for t in range(T):
    n = int(lines[2 * t + 1].strip())
    nums = list(map(int, lines[2 * t + 2].strip().split(" ")))
    nums.sort()
    res = [0 for _ in range(n)]
    res[0] = nums[0]
    for i in range(n):
        if i % 2 == 0:
            res[i] = nums[i // 2]
        else:
            res[i] = nums[-(i + 1) // 2]
    print(" ".join(map(str, res[::-1])))
