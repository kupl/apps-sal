import itertools
n = int(input())
l = list(map(int, input().split()))
ans = 0

for comb in itertools.combinations(l, 3):
    li = list(comb)
    li.sort()
    if li[2] < li[0]+li[1] and li[0] != li[1] != li[2]:
        ans += 1

print(ans)

