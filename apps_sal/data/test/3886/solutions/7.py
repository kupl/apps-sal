import sys
sys.setrecursionlimit(100000)
n = int(input())
s0 = 'What are you doing at the end of the world? Are you busy? Will you save us?'
s1 = 'What are you doing while sending "'
s2 = '"? Are you busy? Will you send "'
s3 = '"?'
(l1, l2, l3) = [len(x) for x in [s1, s2, s3]]
ans = ''


def len_of_string(m):
    return 2 ** m * 143 - 68


def find(i, k):
    if i == 0:
        if k > len(s0):
            return '.'
        else:
            return s0[k - 1]
    else:
        b = len_of_string(i - 1)
        if 1 <= k <= l1:
            return s1[k - 1]
        elif l1 + 1 <= k <= l1 + b:
            return find(i - 1, k - l1)
        elif l1 + b + 1 <= k <= l1 + l2 + b:
            return s2[k - (l1 + b) - 1]
        elif l1 + l2 + b + 1 <= k <= l1 + l2 + 2 * b:
            return find(i - 1, k - (l1 + l2 + b))
        elif l1 + l2 + 2 * b + 1 <= k <= l1 + l2 + l3 + 2 * b:
            return s3[k - (l1 + l2 + 2 * b) - 1]
        else:
            return '.'


for _ in range(n):
    (n, k) = [int(x) for x in input().split()]
    if n > 8698 and k > 295726:
        k -= (n - 1000) * len(s1)
        ans += find(1000, k)
    else:
        ans += find(n, k)
print(ans)
