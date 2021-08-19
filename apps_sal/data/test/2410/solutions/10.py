def maxSubArraySum(a, size):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far


def case():
    n = int(input())
    a = list(map(int, input().split()))
    ans1 = maxSubArraySum(a[1:], n - 1)
    ans2 = maxSubArraySum(a[:-1], n - 1)
    s = sum(a)
    if s > max(ans1, ans2):
        print('YES')
    else:
        print('NO')


for _ in range(int(input())):
    case()
