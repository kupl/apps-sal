q = int(input())
for query in range(q):
    a, b, n, s = map(int, input().split(" "))
    if(s >= n * a):
        s = s - n * a
    else:
        s = s - ((s // n) * n)
    if s > b:
        print("NO")
    else:
        print("YES")
