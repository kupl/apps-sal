from collections import Counter
n = int(input())
c = Counter(list(map(int, input().split())))
if c[1] < c[2]:
    print(c[1])
else:
    print((c[1] - c[2]) // 3 + c[2])
