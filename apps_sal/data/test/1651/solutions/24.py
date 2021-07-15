def solve():
    s, p = list(map(int, input().split()))
    sqrt = int(p ** 0.5) + 1
    for i in range(1, sqrt):
        if p % i == 0:
            if i * (s - i) == p or (p // i) * (s - p // i) == p:
                print("Yes")
                return 

    print("No")

solve()

