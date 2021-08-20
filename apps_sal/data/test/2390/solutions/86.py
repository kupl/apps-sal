def main():
    (N, C) = list(map(int, input().split(' ')))
    sushi = [list(map(int, input().split(' '))) for _ in range(N)]
    cr = [0 for _ in range(N + 1)]
    cr_rt = [0 for _ in range(N + 1)]
    for i in range(N):
        move = sushi[i][0] if i == 0 else sushi[i][0] - sushi[i - 1][0]
        cr[i + 1] = cr[i] + sushi[i][1] - move
        cr_rt[i + 1] = cr_rt[i] + sushi[i][1] - 2 * move
    cl = [0 for _ in range(N + 1)]
    cl_rt = [0 for _ in range(N + 1)]
    for i in range(N):
        move = C - sushi[N - 1 - i][0] if i == 0 else sushi[N - i][0] - sushi[N - 1 - i][0]
        cl[i + 1] = cl[i] + sushi[N - 1 - i][1] - move
        cl_rt[i + 1] = cl_rt[i] + sushi[N - 1 - i][1] - 2 * move
    cr_rt_max = [0 for _ in range(N + 1)]
    cl_rt_max = [0 for _ in range(N + 1)]
    for i in range(N):
        cr_rt_max[i + 1] = max([cr_rt_max[i], cr_rt[i + 1]])
        cl_rt_max[i + 1] = max([cl_rt_max[i], cl_rt[i + 1]])
    ans = 0
    for i in range(N + 1):
        ans = max([ans, cr[i] + cl_rt_max[N - i]])
        ans = max([ans, cl[i] + cr_rt_max[N - i]])
    print(ans)


def __starting_point():
    main()


__starting_point()
