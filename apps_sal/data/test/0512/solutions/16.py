def main():
    n = int(input())
    arr = [[0, 0] for i in range(2 * n + 1)]
    for i in range(n):
        a, b = map(int, input().split())
        if a == -1:
            pass
        elif arr[a] == [0, 0]:
            arr[a] = [i + 1, b]
        else:
            arr[a] = [2**16, 2**16]
        if b == -1:
            pass
        elif arr[b] == [0, 0]:
            arr[b] = [-i - 1, a]
        else:
            arr[b] = [2**16, 2**16]
    ans = [False for i in range(n + 1)]
    ans[0] = True

    for hi in range(2, 2 * n + 2, 2):
        for lo in range(1, hi + 1, 2):
            if not ans[lo // 2]:
                continue
            flag = True
            for i in range(lo, lo + (hi - lo + 1) // 2):
                x, y = arr[i], arr[i + (hi - lo + 1) // 2]
                # print(x,y)
                if x == [0, 0] and y == [0, 0]:
                    continue
                elif x == [0, 0]:
                    if y[0] > 0 or y[1] != -1:
                        flag = False
                        break
                elif y == [0, 0]:
                    if x[0] < 0 or x[1] != -1:
                        flag = False
                        break
                else:
                    if x[0] != -y[0] or x[0] < 0:
                        flag = False
                        break
                    elif x[1] != i + 1 + (hi - lo - 1) // 2 or y[1] != i:
                        flag = False
                        break

            if not flag:
                continue
            ans[hi // 2] = True

    if ans[-1]:
        print("Yes")
    else:
        print("No")
    # print(ans)
    # print(arr)


def __starting_point():
    main()


__starting_point()
