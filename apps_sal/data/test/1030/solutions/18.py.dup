n, p, k = list(map(int, input().split()))
li = []
if p - k > 1:
    li += ['<<']
for i in range(max(1, p - k), min(p + k, n) + 1):
    li += ['(' * int(i == p) + str(i) + ')' * int(i == p)]
li += ['>>' * int(p + k < n)]
print(*li)
