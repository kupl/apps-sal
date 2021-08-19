s1 = set([1, 3, 5, 7, 8, 10, 12])
s2 = set([4, 6, 9, 11])
s3 = set([2])
(a, b) = map(int, input().split())
for i in [s1, s2, s3]:
    if a in i and b in i:
        print('Yes')
        break
else:
    print('No')
