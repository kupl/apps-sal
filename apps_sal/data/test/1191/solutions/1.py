(_, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = list(sorted(zip(a, b, list(range(len(b))))))
d = [0] * len(b)
if k == 0:
    print(' '.join(map(str, b)))
else:
    best = [0] * k
    for (pwr, cnt, index) in c:
        d[index] = sum(best) + cnt
        if cnt > best[0]:
            for i in range(len(best)):
                if cnt <= best[i]:
                    best.insert(i, cnt)
                    best = best[1:]
                    break
            else:
                best = best[1:] + [cnt]
    print(' '.join(map(str, d)))
