n, m = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
rslt = [0]*n
for x in arr:
    rslt[x-1] += 1
print(min(rslt))

