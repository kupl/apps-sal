n, m = map(int, input().split())
arr = [0] * n
cnt = 0
for i in range(n):
    arr[i] = [int(x) for x in input().split()]

for i in range(n):
    for j in range(0, 2 * m, 2):
        try:
            if arr[i][j] == 1 or arr[i][j + 1] == 1:
                cnt += 1
        except:
            pass

print(cnt)
