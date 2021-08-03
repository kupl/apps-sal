import bisect
n = int(input())
a = [(-1) * int(input()) for _ in range(n)]
dp = [10**18 for _ in range(n)]


def lis(a):
    """
    param a: list
    return: the length of Longest increasing subsequence
    (be careful that [list] seq is not the LIS, but its length is accurate LIS length.)
    """
    seq = []
    tmp = 0
    for i in a:
        pos = bisect.bisect_right(seq, i)
        if tmp <= pos:
            seq.append(i)
            tmp += 1
        else:
            seq[pos] = i
    return tmp


print(lis(a))
