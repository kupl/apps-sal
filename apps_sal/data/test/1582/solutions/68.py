import sys
import math

# a != b のとき


def count(a, b, N):

    keta = len(str(N))

    cnt = 0

    # k == 1 なら a == b
    if a == b:
        cnt += 1 if a <= N else 0

    if keta == 1:
        return cnt

    # k == 2 なら ba のみ
    if keta == 2:
        cnt += 1 if b * 10 + a <= N else 0
        return cnt

    # k 桁より少ない数の場合 : 好きな数を間に挟む
    for k in range(2, keta):
        cnt += 10**(k - 2)

    # k 桁の数字の場合
    s = N // (10**(keta - 1))
    t = N % 10
    if b > s:
        return cnt
    elif b < s:
        cnt += 10**(keta - 2)
    else:
        tempN = (N - s * (10**(keta - 1)) - t) // 10
        # print(f"tempN {tempN}")
        cnt += (tempN + 1)  # tempN が 1 なら 0,1 を選べる
        if a > t:
            cnt -= 1

    return cnt


def count_aa(a, N):

    keta = len(str(N))

    cnt = 0

    # keta == 1
    if keta == 1:
        return 1 if a <= N[-1] else 0

    cnt += 1  # a

    # k == 2 なら aa のみ
    if keta == 2:
        return cnt + 1 if a <= N[-1] else 0

    # 3桁以上
    # k 桁より少ない数の場合
    for k in range(2, keta):
        cnt += 10**(k - 2)

    # k 桁の数字の場合
    s = N // (10**(keta - 1))
    t = N % 10
    if b > s:
        return cnt
    elif b < s:
        cnt += 10**(keta - 2)
    else:
        tempN = (N - s * (10**(keta - 1)) - t) // 10
        # print(f"tempN {tempN}")
        cnt += (tempN + 1)  # tempN が 1 なら 0,1 を選べる
        if a > t:
            cnt -= 1

    return cnt


N = int(input())

c = 0
for i in range(1,N+1):
    a = int(str(i)[0])
    b = i % 10
    # print(a,b)
    if b == 0:
        continue
    c += count(a,b,N)

print(c)
