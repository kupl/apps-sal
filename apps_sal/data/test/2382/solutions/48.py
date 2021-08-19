def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    visited = [False] * 2 ** n
    visited[0] = 0
    now = [a[0]]
    for i in range(n):
        new = []
        now2 = 0
        for (j, i) in enumerate(a):
            if visited[j]:
                continue
            if now[now2] > i:
                now2 += 1
                new += [i]
                visited[j] = True
                if now2 == len(now):
                    now += new
                    now.sort(reverse=True)
                    break
        else:
            print('No')
            return
    print('Yes')


main()
