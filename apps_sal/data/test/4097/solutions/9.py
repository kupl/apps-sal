n = int(input())
b = list(map(int, input().split()))
l = len(b)

answer = False
best = 1e9
if l <= 2:
    print(0)
else:
    for start in [b[0] - 1, b[0], b[0] + 1]:
        for end in [b[-1] - 1, b[-1], b[-1] + 1]:
            d = end - start

            canbe = True
            if d % (l - 1) == 0:
                diff = d // (l - 1)
                if d != 0:
                    if diff > 0:
                        needseq = list(range(start, end + 1, diff))
                    else:
                        needseq = list(range(start, end - 1, diff))
                else:
                    needseq = [start] * l
                count = 0
                for s1, s2 in zip(b, needseq):
                    if abs(s1 - s2) <= 1:
                        count += abs(s1 - s2)
                    else:
                        canbe = False
                        break
                if canbe:
                    best = min(best, count)
                    answer = canbe
            else:
                answer = answer or False
    if answer and best != 1e9:
        print(best)
    else:
        print(-1)
