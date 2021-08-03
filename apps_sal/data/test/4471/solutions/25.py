for _ in range(int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    Max = max(X)
    Check = True
    for i in X:
        if (Max - i) % 2 != 0:
            Check = False
            break
    print("YES" if Check else "NO")
