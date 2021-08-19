import sys
lines = sys.stdin.readlines()
# nums = lists(map(int, lines[0].strip().split(" ")))
T = int(lines[0].strip())
for t in range(T):
    (n, k) = list(map(int, lines[2 * t + 1].strip().split(" ")))
    nums = list(map(int, lines[2 * t + 2].strip().split(" ")))
    peaks = [0 for _ in range(n)]

    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peaks[i] = 1
    for i in range(1, n):
        peaks[i] += peaks[i - 1]
    maxP = -1
    maxIndex = -1
    for i in range(n - k + 1):
        if peaks[i + k - 2] - peaks[i] > maxP:
            maxP = peaks[i + k - 2] - peaks[i]
            maxIndex = i
    print("{} {}".format(maxP + 1, maxIndex + 1))
