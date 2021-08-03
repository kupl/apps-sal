t = int(input())
for _ in range(t):
    n, k1, k2 = list(map(int, input().split()))
    a1 = sorted(list(map(int, input().split())))
    a2 = sorted(list(map(int, input().split())))
    if(n in a1):
        print("YES")
    else:
        print("NO")
