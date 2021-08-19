def dist(s):
    return s.find('S') - s.find('G') - 1


(a, b) = map(int, input().split())
dists = [dist(input()) for i in range(a)]
if min(dists) < 0:
    print(-1)
else:
    print(len(set(dists)))
