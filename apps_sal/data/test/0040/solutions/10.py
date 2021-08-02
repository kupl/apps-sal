n = int(input())

ratings = []
is_rated = False
for _ in range(n):
    start, end = [int(p) for p in input().split()]
    if start != end:
        is_rated = True
    ratings.append((start, end))

if is_rated:
    print('rated')
else:
    #
    if list(reversed(sorted(ratings, key=lambda x: x[0]))) == ratings:
        print('maybe')
    else:
        print('unrated')
