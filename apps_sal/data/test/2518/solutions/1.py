N, A, B = list(map(int, input().split()))
H = [0] * (N)
for i in range(N):
    H[i] = int(input())

# めぐる式二分探索
# indexが条件を満たすか判定


def isOK(index, H):
    now_min = index * B
    all_H = []
    for i in range(len(H)):
        if H[i] > now_min:
            all_H.append(H[i] - now_min)
    count = 0
    for j in all_H:
        if j % (A - B) == 0:
            count += int(j // (A - B))
        else:
            count += int(j // (A - B)) + 1
    if count <= index:
        return True
    else:
        return False

# にぶたん
#A : 配列


def binary_search(H):
    N = 10 ** 9 + 1
    ng = -1
    ok = N
    while (abs(ok - ng) > 1):
        mid = int((ok + ng) / 2)
        if isOK(mid, H):
            ok = mid
        else:
            ng = mid
    return ok


print((binary_search(H)))
