def main():
    n = int(input())
    a = [0] + list([int(x) for x in input().split(" ")])
    d = [a[i+1] - a[i] for i in range(len(a)-1)]
    ans = 1
    alist = []
    for i in range(1, n):
        flag = True
        for j in range(n):
            if j >= i and d[j] != d[j-i]:
                flag = False
                break
        if flag:
            alist.append(i)
            ans += 1
    alist.append(n)
    print(ans)
    print(" ".join([str(x) for x in alist]))


def __starting_point():
    main()

__starting_point()
