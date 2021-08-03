query = list(map(int, input().split()))

total = query[3]

sdali = query[0] + query[1] - query[2]
if query[2] > query[1] or query[2] > query[0]:
    print(-1)
elif sdali > total:
    print(-1)
else:
    nesdali = total - sdali
    if nesdali < 1:
        print(-1)
    else:
        print(nesdali)
