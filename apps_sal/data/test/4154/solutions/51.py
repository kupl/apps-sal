
details = list(map(int,input().split()))

N = details[0]
M = details[1]


ab = [list(map(int, input().split())) for _ in range(M)]

smallest_max = ab[0][1]
for i in range(1,M):
    if ab[i][1] < smallest_max:
        smallest_max = ab[i][1]

largest_min = ab[0][0]
for i in range(1,M):
    if ab[i][0] > largest_min:
        largest_min = ab[i][0]



if smallest_max - largest_min >=0:
    print(smallest_max - largest_min + 1)
else:
    print(0)
