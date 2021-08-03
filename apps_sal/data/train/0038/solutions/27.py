t = int(input())
for i in range(t):
    n, k1, k2 = list(map(int, input().split()))
    s1 = max(list(map(int, input().split())))
    s2 = max(list(map(int, input().split())))
    if s1 == n:
        print("YES")
    else:
        print("NO")
