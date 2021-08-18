for _ in range(int(input())):
    L, v, l, r = list(map(int, input().split()))
    ans = L // v - (r // v - (l - 1) // v)
    print(ans)
