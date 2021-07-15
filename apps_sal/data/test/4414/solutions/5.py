q = int(input())
for i in range(q):
    a, b, n, s = map(int, input().split())
    k = s // n
    if k > a:
        p = a * n
    else:
        p = k * n
    if s - p > b:
        print("NO")
    else:
        print("YES")
