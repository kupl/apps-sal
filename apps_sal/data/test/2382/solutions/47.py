def main():
    inf = 10 ** 9 + 5
    n = int(input())
    n2 = 2 ** n
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    # print(s)
    pp = [s[0]]
    s[0] = inf
    for _ in range(n):
        pp.sort()
        i = 1
        np = pp[:]
        while pp:
            p = pp.pop()
            while 1:
                if s[i] < p:
                    np.append(s[i])
                    s[i] = inf
                    break
                else:
                    i += 1
                if i == n2:
                    print("No")
                    return
        pp = np
    print("Yes")


main()
