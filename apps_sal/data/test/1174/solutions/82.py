import copy


def bi_search(money, M, N):
    money.sort()
    left = 0
    right = money[N - 1] + 1
    mid = 0
    while True:
        mid = int((left + right) / 2)
        cnt = 0
        money_tmp = copy.copy(money)
        for i in range(N):
            while True:
                if money_tmp[i] <= mid:
                    break
                else:
                    money_tmp[i] //= 2
                    cnt += 1
        if cnt == M:
            return mid, cnt
        elif cnt < M:
            right = mid
            tmp = cnt
        elif cnt > M:
            left = mid + 1

        if left == right:
            return right, tmp


def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    max_money, cnt = bi_search(A, M, N)
    cnt = M - cnt
    ans = 0
    for i in range(N):
        if max_money >= A[i]:
            continue
        else:
            while True:
                A[i] //= 2
                if max_money >= A[i]:
                    break
    A.sort(reverse=True)
    j = 0
    if A[j] == 0:
        return 0
    for i in range(cnt):
        A[j] //= 2
        j += 1

    for i in range(N):
        ans += A[i]

    return ans


print((main()))
