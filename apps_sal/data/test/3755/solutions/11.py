def main():
    from itertools import accumulate
    n = int(input())
    a = list(map(int, input().split()))
    h = (n + 1) // 2
    m1 = sum([max(i, 0) for i in a[::2]])
    m2 = sum([max(i, 0) for i in a[1::2]])
    m = max(m1, m2)
    if max(a) < 0:
        m = max(a)
    flag = False
    ans = []
    if m == m1 or m == m2:
        if m2 == m:
            n -= 1
            h = (n + 1) // 2
            a.pop(0)
            ans.append(1)
        for i in range(h):
            if a[2 * i] < 0:
                if flag == False:
                    ans.append(1)
                    ans.append(1)
                else:
                    ans.append(3)
            else:
                if flag:
                    ans.append(2)
                else:
                    flag = True
        if ans[-1] == 3 or n % 2 == 0:
            ans.append(2)
    else:
        for i in range(n):
            if a[i] != m:
                ans.append(1)
            else:
                for j in range(n - i, 1, -1):
                    ans.append(j)
                break
    print(m)
    print((len(ans)))
    for i in ans:
        print(i)


main()
