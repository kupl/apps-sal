n = int(input())
arr = [int(x) for x in input().split(' ')]
paired, fixpoints = 0, 0
for x in range(n):
    if arr[x] == x: fixpoints += 1
    else:
        if arr[arr[x]] == x: paired += 1
if fixpoints == n:
    print(fixpoints)
elif paired > 0:
    print(fixpoints+2)
else:
    print(fixpoints+1)

