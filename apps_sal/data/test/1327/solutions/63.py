from itertools import product
(N, M) = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(N)]
ans = []
for lst in product([-1, 1], repeat=3):
    temp = []
    for (x, y, z) in xyz:
        temp.append(x * lst[0] + y * lst[1] + z * lst[2])
    temp.sort(reverse=True)
    ans.append(sum(temp[:M]))
print(max(ans))
