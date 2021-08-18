N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
bc = [0] * M
for i in range(M):
    bc[i] = list(map(int, input().split()))
bc = sorted(bc, key=lambda x: x[1], reverse=True)


# めぐる式二分探索
# indexが条件を満たすか判定
def isOK(index, key, A):
    if A[index] < key:
        return True
    else:
        return False

# にぶたん
#A : 配列


def binary_search(key, A):
    N = len(A)
    ng = -1
    ok = N
    while (abs(ok - ng) > 1):
        mid = int((ok + ng) / 2)
        if isOK(mid, key, A):
            ok = mid
        else:
            ng = mid
    return ok

#a = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]


# print(A)
#print(binary_search(5, A))
# 二分探索の結果がそれを超える枚数
fix = 0
fix2 = 0
fix3 = 0
ans = 0
for i in range(M):
    now = bc[i]
    x = binary_search(now[1], A)
    fix = x
    fix3 = now[0]
    #print(fix, fix2, fix3, ans)
    if fix + fix2 + fix3 >= N:
        fix3 = N - fix - fix2
        ans += sum(A[:fix]) + now[1] * fix3
        print(ans)
        return
    else:
        fix2 += fix3
        ans += now[0] * now[1]


ans += sum(A[:(N - fix2)])
print(ans)
