n, k = list(map(int, input().split()))


inF = False
bad = 0
last = None
stretches = [0]
for d in [int(x) >= 0 for x in input().split()]:
    last = d
    if d and not inF:
        continue
    else:
        inF = True
        if d:
            stretches[-1] += 1
        else:
            bad += 1
            if stretches[-1] != 0:
                stretches.append(0)

if bad > k:
    print(-1)
elif bad == 0:
    print(0)
elif n == k:
    print(1)
else:
    k -= bad

    num = 1

    if last:
        num -= 1

    if stretches[-1] == 0:
        del stretches[-1]

    num_ = num
    stretches_ = stretches[:-1]
    k_ = k

    if len(stretches) > 0:
        num += (len(stretches)) * 2
        last = stretches[-1]
        stretches.sort()

        while len(stretches) > 0 and stretches[0] <= k:
            num -= 2
            k -= stretches[0]
            del stretches[0]

        if not last in stretches:
            num += 1

    if len(stretches_) > 0:
        num_ += (len(stretches_) + 1) * 2
        stretches_.sort()

        while len(stretches_) > 0 and stretches_[0] <= k_:
            num_ -= 2
            k_ -= stretches_[0]
            del stretches_[0]

        print(min(num, num_))
    else:
        print(num)
