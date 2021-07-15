n,k = list(map(int, input().strip().split()))

a = list(map(int, input().strip().split()))

maks = 0

for e in a:
    if k % e == 0:
        maks = max(maks,e)

print(k//maks)

