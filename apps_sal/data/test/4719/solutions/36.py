# C - 怪文書
def main():
    n = int(input())
    ans = list(input())

    for _ in range(n - 1):
        s = list(input())
        temp = []
        for j in ans:
            if j in s:
                s.remove(j)
                temp.append(j)
        else:
            ans = temp
    else:
        ans.sort()
        print((''.join(ans)))


def __starting_point():
    main()


__starting_point()
