l, r = list(map(int, input().split()))

for i in range(l, r+1):

    S = str(i)
    used = set()
    for s in S:
        used.add(s)
    if len(S) == len(used):
        print(S)
        return
print(-1)

