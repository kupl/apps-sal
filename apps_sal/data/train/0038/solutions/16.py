for _ in range(int(input())):
    n,k1A,k2A = list(map(int,input().split()))
    k1 = list(map(int,input().split()))
    k2 = list(map(int,input().split()))
    print("YES" if max(k1) > max(k2) else "NO")
