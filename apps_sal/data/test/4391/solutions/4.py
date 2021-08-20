def max_average(nums, k):

    def get_delta(avg, nums, k):
        n = len(nums)
        accu = [0.0] * (n + 1)
        minval_pos = None
        delta = 0.0
        for i in range(n):
            accu[i + 1] = nums[i] + accu[i] - avg
            if i >= k - 1:
                if minval_pos == None or accu[i - k + 1] < accu[minval_pos]:
                    minval_pos = i - k + 1
                if accu[i + 1] - accu[minval_pos] >= 0:
                    delta = max(delta, (accu[i + 1] - accu[minval_pos]) / (i + 1 - minval_pos))
        return delta
    (left, delta) = (min(nums), float('inf'))
    while delta > 1e-06:
        delta = get_delta(left, nums, k)
        left += delta
    return left


def f(arr, k):
    return max_average(arr, k)


(n, k) = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
print(f(arr, k))
