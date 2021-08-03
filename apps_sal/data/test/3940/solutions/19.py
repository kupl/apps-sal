import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
ans = n
lists = []
#
for k in range(m):
    st, en = list(map(int, input().split()))

    ans = min(ans, en - st + 1)

print(ans)

for i in range(n):
    lists.append(str(i % ans))

print(' '.join(lists))
