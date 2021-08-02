n = int(input())
pieces = []

sum_total = 0
sum_left = 0
for i in range(1, n + 1):
    keys = []
    piece = input().split()
    keys = [int(x) for x in piece]
    sum_total += sum(keys)
    pieces.append(keys)

canrotate = False
for i in range(n):
    sum_left += pieces[i][0]
    if pieces[i][0] % 2 != pieces[i][1] % 2:
        canrotate = True

if sum_total % 2 == 1:
    print(-1)
elif not canrotate and sum_left % 2 == 1:
    print(-1)
elif sum_left % 2 == 1:
    print(1)
else:
    print(0)
