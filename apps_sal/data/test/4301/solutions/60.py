def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    sortA = sorted(A)
    ans = sortA[N - 1]
    ans2 = sortA[N - 2]
    if ans == ans2:
        flag = 1
    else:
        flag = 0
    for i in range(N):
        if flag == 1:
            print(ans)
        elif A[i] == ans:
            print(ans2)
        else:
            print(ans)


main()
