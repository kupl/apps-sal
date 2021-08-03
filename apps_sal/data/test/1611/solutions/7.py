input()
arr = list(map(int, input().split()))
ans = 0
tmp = sum(arr)
for i in arr:
    if i * 2 >= tmp:
        ans = 2 * i - tmp + 1
        break
print(ans)
