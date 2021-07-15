def main():
    mod = 10**9+7
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort(key=lambda x: -abs(x))
    kouho = []
    minus = 0
    last_plus = None
    last_minus = None
    if k == 1:
        print((max(a)))
        return
    for i in range(k):
        kouho.append(a[i])
        if a[i] >= 0:
            last_plus = a[i]
        if a[i] < 0:
            minus += 1
            last_minus = a[i]
    if minus % 2 == 0:
        ans = 1
        for i in kouho:
            ans = ans*i % mod
        print(ans)
        return
    change_plus = None
    change_minus = None
    if last_plus != None:
        # マイナスを追加する
        for i in range(k, n):
            if a[i] <= 0:
                change_plus = a[i]
                break
    if last_minus != None:
        # マイナスを追加する
        for i in range(k, n):
            if a[i] >= 0:
                change_minus = a[i]
                break

    # print(kouho)
    #print(last_plus, change_plus)
    #print(last_minus, change_minus)

    if change_plus == None and change_minus == None:
        ans = 1
        for i in range(k):
            ans = ans*a[-i-1] % mod
    elif change_plus == None:
        ans = change_minus
        for i in kouho:
            ans = ans*i % mod
        ans = ans*pow(last_minus, mod-2, mod) % mod
    elif change_minus == None:
        ans = change_plus
        for i in kouho:
            ans = ans*i % mod
        ans = ans*pow(last_plus, mod-2, mod) % mod
    else:
        if abs(change_plus*last_minus) < abs(change_minus*last_plus):
            ans = change_minus
            for i in kouho:
                ans = ans*i % mod
            ans = ans*pow(last_minus, mod-2, mod) % mod
        else:
            ans = change_plus
            for i in kouho:
                ans = ans*i % mod
            ans = ans*pow(last_plus, mod-2, mod) % mod
    print(ans)


main()

