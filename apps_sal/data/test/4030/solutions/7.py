import sys
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__


def ceil(tails, L, R, key):
    while L + 1 < R:
        m = (L + R) // 2
        if key < tails[m]:
            L = m
        else:
            R = m
    return R


def LIS(a, n):
    tails = [0] * (n + 1)
    tails[0] = a[0]
    seq_len = 1
    for i in range(1, n):
        if a[i] > tails[0]:
            tails[0] = a[i]
            ans.append(1)
        elif a[i] < tails[seq_len - 1]:
            tails[seq_len] = a[i]
            seq_len += 1
            ans.append(seq_len)
        else:
            pos = ceil(tails, -1, seq_len - 1, a[i])
            tails[pos] = a[i]
            ans.append(pos + 1)
    return seq_len


n = int(input())
s = input()
ans = [1]
res = LIS(s, n)
print(res)
print(*ans)
