N, K, *AB = [int(a)for a in open(0).read().split()]
AB = sorted(zip(AB[::2], AB[1::2]))
cnt = 0
for a, b in AB:
    cnt += b
    if cnt >= K:
        print(a)
        return
