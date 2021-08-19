def mi():
    return list(map(int, input().split()))


'\n5\n6 1 6 6 0\n'
n = int(input())
a = list(mi())
t = max(a)
cnt = 0
i = 0
while i < n:
    if a[i] == t:
        curcnt = 0
        while i < n and a[i] == t:
            curcnt += 1
            i += 1
        cnt = max(cnt, curcnt)
    i += 1
print(cnt)
