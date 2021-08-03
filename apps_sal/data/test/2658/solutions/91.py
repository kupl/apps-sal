# 入力:N,M(int:整数)
def input2():
    return map(int, input().split())

# 入力:[n1,n2,...nk](int:整数配列)


def input_array():
    return list(map(int, input().split()))


n, k = input2()
A = input_array()

# ある地点から循環に陥る
judge = [True] * n
tmps = [1]  # 循環手前
count = 0  # 参照地点

for i in range(2 * (10**5) + 1):
    if judge[count] == True:
        judge[count] = False
        count = A[count] - 1
        tmps.append(count + 1)
    else:
        break

loop_st = tmps.index(tmps[-1])
loops = tmps[loop_st:-1]


if k < loop_st:
    print(tmps[k])
else:
    k = k - loop_st
    k %= len(loops)
    print(loops[k])
