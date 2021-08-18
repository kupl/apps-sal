n = int(input())
cubes = list(map(int, input().split()))
col = cubes[n - 1]
pos = n - 1
i = n - 1
while(i > -1):
    if(col == cubes[i]):
        col = cubes[i]
    else:
        print(i + 2)
        break
    i -= 1
else:
    print(1)
