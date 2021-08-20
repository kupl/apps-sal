def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    used = [False] * n
    napr = True
    c = 0
    ans = 0
    while False in used:
        if napr:
            for i in range(n):
                if c >= arr[i] and used[i] == False:
                    used[i] = True
                    c += 1
        else:
            for i in range(n - 1, 0 - 1, -1):
                if c >= arr[i] and used[i] == False:
                    used[i] = True
                    c += 1
        napr = not napr
        if False in used:
            ans += 1
    print(ans)


main()
