import collections
n = int(input())
a = [0] + list(map(int, input().split()))

a_pos = [a[i] + i for i in range(1, n + 1)]
a_neg = [-a[i] + i for i in range(1, n + 1)]

c_pos = collections.Counter(a_pos)
c_neg = collections.Counter(a_neg)

ans = 0
for c in c_pos:
    ans += c_pos[c] * c_neg[c]

print(ans)
