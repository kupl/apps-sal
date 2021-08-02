t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    s = set(a)
    if len(s) == max(s) - min(s) + 1:
        print("YES")
    else:
        print("NO")
