def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1

    ans = dict()

    for i in range(n):
        # st = i + 1
        if i not in ans:
            p = []

            j = i
            p.append(j)
            ca = 0
            while True:
                ca += 1
                j = a[j]
                p.append(j)
                if j == i:
                    for x in p:
                        ans[x] = ca
                    break

    for i in range(n):
        print(ans   [i], end=" ")
    print()


for _ in range(int(input())):
    solve()

