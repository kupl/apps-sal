q = int(input())
for query in range(q):
    m, n = list(map(int, input().split()))
    if m - n <= 1:
        print("NO")
    else:
        print("YES")
