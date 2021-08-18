import bisect
n = int(input())
num_list = list(map(int, input().split()))


def LongestIncreasingSubsequence(a, n):
    min_lis = []
    for i in range(n):
        pos = bisect.bisect_left(min_lis, a[i])
        if pos == len(min_lis):
            min_lis.append(a[i])
        else:
            min_lis[pos] = a[i]
    return (len(min_lis))


print(LongestIncreasingSubsequence(num_list, n))
