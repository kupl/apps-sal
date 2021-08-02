n = int(input())
# =map(int,input().split())
arr = list(map(int, input().split()))
c = [0] * 1
c[0] = 1
for i in range(1, n):
    if arr[i] == arr[i - 1]:
        c[-1] += 1
    else:
        c.append(1)
ans = 0
for i in range(len(c) - 1):
    k = min(c[i], c[i + 1])
    if k > ans:
        ans = k
print(2 * ans)
