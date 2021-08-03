D, N = map(int, input().split())
count = 0

if D == 0:
    for i in range(N):
        count += 1
    if N == 100:
        count += 1
    print(count)
elif D == 1:
    for i in range(N):
        count += 100
    if N == 100:
        count += 100
    print(count)
elif D == 2:
    for i in range(N):
        count += 10000
    if N == 100:
        count += 10000
    print(count)
