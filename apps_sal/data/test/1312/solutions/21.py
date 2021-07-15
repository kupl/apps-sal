n,m = map(int, input().split())
cur = n;
for i in range(0,m):
    print( cur // (m - i),end = ' ')
    cur -= cur // (m - i)

