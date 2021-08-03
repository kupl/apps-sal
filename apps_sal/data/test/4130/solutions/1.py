n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
l = [0 for i in range(150150)]
for val in arr:
    for j in range(-1, 2):
        if val + j == 0:
            continue
        if l[val + j] == 0:
            l[val + j] = 1
            break
ans = 0
for i in range(1, 150150):
    ans += l[i]
print(ans)
