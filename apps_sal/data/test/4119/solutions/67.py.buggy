n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
if n >= m:
    print(0)
    return
dis = [x[i + 1] - x[i] for i in range(m - 1)]
dis.sort()
if n > 1:
    del dis[-(n - 1):]
print(sum(dis))
