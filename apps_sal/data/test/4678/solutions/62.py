N = int(input())
A = list(map(int, input().split()))
tot = 0
for i, a in enumerate(A):
    if i == 0:
        forward = a
        continue
    if forward >= a:
        tot += forward - a
    else:
        forward = a
print(tot)
