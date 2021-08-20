from itertools import permutations
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
ans = 0
p = list(permutations(range(n), n))
for L in p:
    s = L[0]
    for i in L[1:]:
        ans += ((l[s][0] - l[i][0]) ** 2 + (l[s][1] - l[i][1]) ** 2) ** 0.5
        s = i
print(ans / len(p))
