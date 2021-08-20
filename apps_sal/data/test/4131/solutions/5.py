from collections import defaultdict
import bisect
(N, M) = map(int, input().split())
dic = defaultdict(list)
cities = []
for _ in range(M):
    (p, y) = map(int, input().split())
    cities.append([p, y])
for item in sorted(cities):
    dic[item[0]].append(item[1])
for item in cities:
    print('%06d%06d' % (item[0], bisect.bisect(dic[item[0]], item[1])))
