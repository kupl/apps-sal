n = int(input())
num = list(map(int, input().split()))
used = [False] * 200001
for i in range(len(num) - 1, -1, -1):
    if not used[num[i]]:
        used[num[i]] = True
        ans = num[i]
print(ans)
