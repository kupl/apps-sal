from collections import defaultdict

def solve(n, k, nums):
    nums.sort()

    new_nums = [0]
    for i in range(1, n):
        x = min(nums[i] - nums[i-1], 6)
        new_nums.append(new_nums[-1] + x)

    cand_count = new_nums[-1] + 1
    candidates = [0] * cand_count

    for n in new_nums:
        for i in range(n-5, n+1):
            if 0 <= i < cand_count:
                candidates[i] += 1

    prev = [None] * cand_count
    max_val = 0
    for i in range(cand_count):
        max_val = max(max_val, candidates[i])
        prev[i] = max_val
        
    for ki in range(1, k):
        new = [None] * cand_count
        new[0:6] = prev[0:6]
        for i in range(6, cand_count):
            new[i] = max(new[i-1], prev[i-6]+candidates[i])
        prev = new
        
    print(prev[-1])


def solve_from_stdin():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    solve(n, k, nums)

def test():
    n, k = 1000, 500
    nums = list(range(n))
    solve(n, k, nums)

solve_from_stdin()
