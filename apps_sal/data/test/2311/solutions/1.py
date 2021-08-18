def count(A):
    segs = []
    cur = 0
    flag = 0
    for a in A:
        if a:
            cur += 1
            flag = 1
        else:
            if flag:
                flag = 0
                segs.append(cur)
                cur = 0
    if flag and (cur > 0):
        segs.append(cur)
    count = [0] * (len(A) + 1)
    for s in segs:
        for i in range(1, s + 1):
            count[i] += (s - i + 1)
    return count


def f():
    n, m, k = [int(s) for s in input().split()]
    A = [int(s) for s in input().split()]
    B = [int(s) for s in input().split()]
    ans = 0
    countA = count(A)
    countB = count(B)
    for l1 in range(1, n + 1):
        if k % l1:
            continue
        l2 = k // l1
        if l2 > m:
            continue
        ans += countA[l1] * countB[l2]
    print(ans)


f()
