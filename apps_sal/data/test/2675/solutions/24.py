n, m = list(map(int, input().split()))
arr = []
for i in range(n):
    l = list(map(int, input().split()))
    arr.append([l[0] * l[1], 0, l[0]])
for i in range(m):
    l = list(map(int, input().split()))
    arr.append([l[0] * l[1], 1, l[0]])
arr.sort()
i = 0
ans = 0
while(i < m + n):
    if(arr[i][1] == 1):
        i += 1
    else:
        w = i
        for j in range(i, m + n + 1):
            if(j != m + n and arr[j][0] == arr[i][0]):
                if(arr[j][1] == 1 and w == i):
                    w = j
            else:
                break
        ans += min(w - i, j - w)
        i = j
print(ans)
