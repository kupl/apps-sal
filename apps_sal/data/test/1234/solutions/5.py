def main():
    (n, m, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ret = sum(a)
    index = list(range(n))
    index.sort(key=lambda i: a[i])
    rm_flag = [False] * n
    for i in range(n - m * k):
        rm_flag[index[i]] = True
        ret -= a[index[i]]
    (pos, cnt) = ([], 0)
    for i in range(n):
        if not rm_flag[i]:
            cnt += 1
            if cnt == m:
                pos.append(i + 1)
                cnt = 0
                if len(pos) == k - 1:
                    break
    print(ret)
    print(*pos)


def __starting_point():
    main()


__starting_point()
