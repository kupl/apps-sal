n, x, y = map(int, input().split())
l = list(map(int, input().split()))
for d in range(n):
    ad = l[d]
    valid = True
    for j in range(max(d - x, 0), d):
        if (ad >= l[j]):
            valid = False
    for j in range(d + 1, min(d + y + 1, n)):
        if (ad >= l[j]):
            valid = False
    if(valid):
        print(d + 1)
        quit()
