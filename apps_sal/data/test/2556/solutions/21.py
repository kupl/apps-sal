for _ in range(int(input())):
    c, sm = list(map(int, input().split()))
    ans = ((sm // c + 1)**2) * (sm % c) + ((sm // c)**2) * (c - sm % c)
    print(ans)

