from itertools import accumulate, combinations
seconds_since_boot = int(input())
arr = [0] + list(accumulate(map(lambda x: int(x) - 100, input().split())))
longest = 0
for start, end in combinations(range(seconds_since_boot + 1), 2):
    if end - start > longest and arr[end] - arr[start] > 0:
        longest = end - start
print(longest)
