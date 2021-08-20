(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
ret = 0
cur = 1
for i in a:
    ret += i - cur
    if i < cur:
        ret += n
    cur = i
print(ret)
