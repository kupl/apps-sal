t = int(input())
for rew in range(t):
    n = int(input())
    if n % 4 == 2:
        print("NO")
    else:
        print("YES")
        n //= 2
        pocz = [2 * (i + 1) for i in range(n)]
        kon = [2 * i + 1 for i in range(n - 1)]
        dod = sum(pocz) - sum(kon)
        odp = pocz + kon + [dod]
        print(*odp)
