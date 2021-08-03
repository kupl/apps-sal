n, m = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(input())
ans = 0
ent = list(map(int, input().split()))
count = [0] * 5
for i in range(m):
    for j in range(n):
        count[ord(arr[j][i]) - 65] += ent[i]
    ans += max(count)
    count = [0, 0, 0, 0, 0]
print(ans)
