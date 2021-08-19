(n, h) = list(map(int, input().split()))
pr = 0
for s in input().split():
    if int(s) > h:
        pr += 1
print(n + pr)
