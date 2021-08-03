def main():

    N, K, C = [int(i) for i in input().split()]
    S = input().rstrip()

    if all(s == "x" for s in S):
        return

    left = [0] * N
    day = 0
    work_cnt = 1
    while day < N:
        if S[day] == "o":
            left[day] = work_cnt
            work_cnt += 1
            day += C
        day += 1

    right = [0] * N
    day = N - 1
    work_cnt = K
    while 0 <= day:
        if S[day] == "o":
            right[day] = work_cnt
            work_cnt -= 1
            day -= C
        day -= 1

    for i in range(N):
        if left[i] == right[i] and left[i] != 0:
            print((i + 1))


main()
