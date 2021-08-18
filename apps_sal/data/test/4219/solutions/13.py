

N = int(input())
xy_list = []
for _ in range(N):
    A = int(input())
    xy = []
    for _ in range(A):
        xy.append(list(map(int, input().split())))
    xy_list.append(xy)


ans = 0
for i in range(2**N):
    for j, a_list in enumerate(xy_list):
        if (i >> j) & 1 == 1:
            for k, (x, y) in enumerate(a_list):
                if (i >> (x - 1)) & 1 != y:
                    break
            else:
                continue
            break
    else:
        ans = max(ans, bin(i)[2:].count("1"))
print(ans)
