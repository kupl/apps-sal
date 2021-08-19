(n, n1, n2) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
(n1, n2) = (min(n1, n2), max(n1, n2))
to_consider = a[-n1 - n2:]
(pa, pb) = (to_consider[:n2], to_consider[n2:])
print(float(sum(pa)) / len(pa) + float(sum(pb)) / len(pb))
