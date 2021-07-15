I = lambda : map(int, input().split())
n, = I()
arr = []
for i in range(0, n):
    arr.append(list(I()))

for x in range(0, n):
    for y in range(0, n):
        if arr[x][y] != 1:
            found = False
            for s in range(0, n):
                for t in range(0, n):
                    if arr[x][y] == arr[x][s] + arr[t][y]:
                        found = True
            if not found:
                print("No")
                return
print("Yes")
