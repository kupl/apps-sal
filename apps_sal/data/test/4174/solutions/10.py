(n, x) = map(int, input().split())
L = list(map(int, input().split()))
cnt = 1
d = 0
for l in L:
    d += l
    if d <= x:
        cnt += 1
    else:
        break
print(cnt)
