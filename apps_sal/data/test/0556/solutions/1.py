(l, r, k) = map(int, input().split())
curr = 1
cnt = 0
while curr <= r:
    if curr >= l:
        print(curr, end=' ')
        cnt += 1
    curr *= k
if cnt == 0:
    print(-1)
