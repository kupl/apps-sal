def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    p = list(map(int, input().split()))
    c = [-1] * n
    for i in range(n):
        p[i] -= 1
        c[p[i]] = i
    r = [False] * (n - 1)
    ans = []
    for i in range(n):
        j = c[i]
        while j != i:
            if r[j - 1]:
                print(-1)
                return
            ans.append(j)
            r[j - 1] = True
            p[j - 1], p[j] = p[j], p[j - 1]
            c[p[j]] = j
            c[p[j - 1]] = j - 1
            j -= 1
    for i in r:
        if not i:
            print(-1)
            return
    for i in ans:
        print(i)


main()
