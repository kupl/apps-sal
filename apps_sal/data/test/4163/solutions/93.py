N = int(input())
(curr, prev, twice, thrice) = (False, False, False, False)
for i in range(0, N):
    row = input()
    curr = row[0] == row[2]
    thrice = thrice or (twice and curr)
    twice = curr and prev
    prev = curr
if thrice:
    print('Yes')
else:
    print('No')
