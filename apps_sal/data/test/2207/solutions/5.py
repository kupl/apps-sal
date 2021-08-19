def read():
    return list(map(int, input().split()))


(n, m) = read()
a = [input() for i in range(n)]
s = a[n - 1].split('.')
cnt = len(s) - s.count('')
print(cnt)
