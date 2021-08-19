(n, k) = map(int, input().split())
l = [int(i) for i in input().split()]
l.sort(reverse=True)
elems = []
j = -1
cnt = 0
for i in range(n):
    if cnt == k:
        break
    j += 1
    fixed = l[0:j]
    for z in range(j, n):
        if cnt == k:
            continue
        print(j + 1, *fixed + [l[z]])
        cnt += 1
        if cnt == k:
            break
