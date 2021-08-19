def main():
    n = int(input())
    a = list(map(int, input().split()))
    (cnt_z, cnt_n, idx) = (0, 0, -1)
    z_idx = []
    a.append(-10 ** 9 - 1)
    for i in range(n):
        if a[i] < 0:
            cnt_n += 1
            idx = i if a[idx] < a[i] else idx
        elif not a[i]:
            cnt_z += 1
            z_idx.append(i)
    if cnt_z == n or (cnt_z == n - 1 and cnt_n == 1):
        for i in range(n - 1):
            print(1, i + 1, i + 2)
        return
    used = [0 for i in range(n)]
    for i in range(cnt_z - 1):
        print(1, z_idx[i] + 1, z_idx[i + 1] + 1)
        used[z_idx[i]] = 1
    if cnt_n % 2 and cnt_z:
        print(1, idx + 1, z_idx[-1] + 1)
        used[idx] = 1
    elif cnt_n % 2:
        z_idx.append(idx)
    if len(z_idx):
        print(2, z_idx[-1] + 1)
        used[z_idx[-1]] = 1
    lst = -1
    for i in range(n):
        if not used[i]:
            if lst != -1:
                print(1, lst + 1, i + 1)
            lst = i


def __starting_point():
    main()


__starting_point()
