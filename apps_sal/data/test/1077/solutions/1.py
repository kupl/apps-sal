n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
count_good = [[0, i + 1] for i in range(m)]
bad = 0
bad_places = []
good_places = [[i + 1, []] for i in range(m)]
for i in range(len(A)):
    elem = A[i]
    if elem <= m:
        count_good[elem - 1][0] += 1
        good_places[elem - 1][1].append(i)
    else:
        bad += 1
        bad_places.append(i)
ideal = n // m
for elem in good_places:
    bad_places.extend(elem[1][ideal:])
bad = len(bad_places)
badd = bad
count_good.sort()
minn = count_good[0][0]
bad_Cnt = 0
while minn != ideal:
    j = 0
    while j < len(count_good) and count_good[j][0] == minn and bad > 0:
        count_good[j][0] += 1
        A[bad_places[bad_Cnt]] = count_good[j][1]
        bad_Cnt += 1
        bad -= 1
        j += 1
    minn += 1
print(minn, badd - bad)
print(*A)

