def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


def main():
    t = int(input())
    ans = []
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        total = sum(arr)
        sum1 = maxSubArraySum(arr[:n - 1], n - 1)
        sum2 = maxSubArraySum(arr[1:], n - 1)
        if total > max(sum1, sum2):
            ans.append('YES')
        else:
            ans.append('NO')

    for i in ans:
        print(i)


main()
