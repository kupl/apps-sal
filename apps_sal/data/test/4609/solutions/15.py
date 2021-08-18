

def main():
    N = int(input())
    ans = 0
    dic = {}
    for _ in range(N):
        a = int(input())
        if a not in list(dic.keys()):
            dic[a] = 1
            ans += 1
        elif dic[a] == 0:
            dic[a] += 1
            ans += 1
        else:
            dic[a] -= 1
            ans -= 1

    print(ans)


def __starting_point():
    main()


__starting_point()
