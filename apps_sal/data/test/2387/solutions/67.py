def main():
    n = int(input())
    l_0 = []
    r_0 = []
    ls_plus = []
    ls_minus = []
    sum_l = 0
    sum_r = 0
    for i in range(n):
        s = input()
        left, right = 0, 0
        for j in range(len(s)):
            if s[j] == '(':
                right += 1
            else:
                if right > 0:
                    right -= 1
                else:
                    left += 1
        if left == right == 0:
            continue

        if left == 0:
            l_0.append((left, right))
        elif right == 0:
            r_0.append((left, right))
        elif left < right:
            ls_plus.append((left, right))
        else:
            ls_minus.append((left, right))
        sum_l += left
        sum_r += right

    if len(ls_plus) == len(ls_minus) == len(l_0) == len(r_0) == 0:
        print("Yes")
        return

    if len(l_0) == 0 or len(r_0) == 0:
        print("No")
        return
    if sum_l != sum_r:
        print("No")
        return

    # r-lの大きい順
    ls_plus.sort(key=lambda x: x[1] - x[0], reverse=True)
    # lの小さい順
    ls_plus.sort(key=lambda x: x[0])

    # l-rの小さい順
    ls_minus.sort(key=lambda x: x[0] - x[1])
    # lの大さい順
    ls_minus.sort(key=lambda x: x[0], reverse=True)

    now_r = 0
    for ll in l_0:
        now_r += ll[1]

    for _ in ls_plus:
        r = _[1]
        x = now_r - _[0]
        if x >= 0:
            now_r = x + r
        else:
            print("No")
            return

    for _ in ls_minus:
        r = _[1]
        x = now_r - _[0]
        if x >= 0:
            now_r = x + r
        else:
            print("No")
            return

    print("Yes")


main()
