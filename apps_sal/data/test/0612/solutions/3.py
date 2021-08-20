def solve():
    (n, k, p) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    even = list([x for x in a if x % 2 == 0])
    odd = list([x for x in a if x % 2 == 1])
    if (len(odd) - (k - p)) % 2 != 0:
        print('NO')
        return
    ans = [[] for i in range(k)]
    for i in range(k - p):
        if odd:
            ans[i].append(odd.pop())
        else:
            print('NO')
            return
    for i in range(k - p, k):
        if even:
            ans[i].append(even.pop())
        elif len(odd) >= 2:
            ans[i].append(odd.pop())
            ans[i].append(odd.pop())
        else:
            print('NO')
            return
    ans[0] += even + odd
    print('YES')
    for part in ans:
        print(len(part), ' '.join(map(str, part)))


def __starting_point():
    solve()


__starting_point()
