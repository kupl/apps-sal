def main():
    n = int(input())
    deg = [0] * n
    for i in range(n - 1):
        u, v = map(int, input().split())
        deg[u - 1] += 1
        deg[v - 1] += 1
    count = 0
    ans = 0
    e = []
    for i in range(n):
        if (deg[i] > 2):
            count += 1
            ans = i
        if (deg[i] == 1):
            e.append(i)
    if (count > 1):
        print("No")
    else:
        print("Yes")
        print(deg[ans])
        for el in e:
            if (el != ans):
                print(ans + 1, el + 1)


main()
