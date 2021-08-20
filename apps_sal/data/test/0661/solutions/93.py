(m, k) = map(int, input().split())
if m == 1:
    if k == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
elif 2 ** m <= k:
    print(-1)
else:
    remain = set(range(2 ** m))
    use = set()
    count = 0
    while k:
        if k & 1:
            remain.remove(2 ** count)
            use.add(2 ** count)
        k >>= 1
        count += 1
    ans = []
    remain = list(remain)
    use = list(use)
    for i in remain:
        ans.append(str(i))
    for i in use:
        ans.append(str(i))
    for i in remain[::-1]:
        ans.append(str(i))
    for i in use[::-1]:
        ans.append(str(i))
    print(' '.join(ans))
