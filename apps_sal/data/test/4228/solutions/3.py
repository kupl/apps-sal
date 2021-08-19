(N, L) = list(map(int, input().split()))
azi2 = []
azi = [L + i for i in range(N)]
for i in azi:
    azi2.append(abs(i))
if 0 in azi:
    print(sum(azi))
else:
    mi = azi2.index(min(azi2))
    del azi[mi]
    print(sum(azi))
