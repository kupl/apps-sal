def main():
    n = int(input())
    a = [0]
    a += list(map(int, input().split()))
    p = [0] * 200001
    p[1] = 0
    k = [-1] * 200001
    k[0] = 1
    ans = 1
    cnt = 1
    for i in range(1, n + 1):
        if i == 1:
            if a[i] == 1:
                cnt += 1
                k[i] = cnt
                p[cnt] = i
                ans += 1
            else:
                k[i] = k[a[a[i]]]
                p[k[i]] = i
        elif p[k[a[i]]] != a[i]:
            cnt += 1
            k[i] = cnt
            p[cnt] = i
            ans += 1
        else:
            k[i] = k[a[i]]
            p[k[i]] = i
    print(ans)


main()
