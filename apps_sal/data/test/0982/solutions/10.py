t = int(input())
for i in range(t):
    l, r = list(map(int, input().split()))
    if 2 * l >= (r + 1):
        print("YES")
    else:
        print("NO")

