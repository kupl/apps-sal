def main():
    (N, K) = list(map(int, input().split()))
    (R, S, P) = list(map(int, input().split()))
    T = input()
    dict = {'r': P, 's': R, 'p': S}
    check = []
    ans = 0
    for i in range(N):
        if i - K < 0:
            ans += dict[T[i]]
            check.append(1)
        elif T[i - K] != T[i]:
            ans += dict[T[i]]
            check.append(1)
        elif T[i - K] == T[i]:
            if i - 2 * K < 0:
                ans += 0
                check.append(0)
            elif T[i - 2 * K] == T[i]:
                if check[i - K] == 1:
                    ans += 0
                    check.append(0)
                else:
                    ans += dict[T[i]]
                    check.append(1)
            else:
                ans += 0
                check.append(0)
    return ans


print(main())
