N = int(input())
A = list(map(int, input().split()))
full_root = [0] + A + [0]
full_place = [abs(full_root[i] - full_root[i + 1]) for i in range(N + 1)]
full_res = sum(full_place)
for ind in range(1, N + 1):
    res = full_res - sum(full_place[ind - 1:ind + 1]) + abs(full_root[ind - 1] - full_root[ind + 1])
    print(res)
