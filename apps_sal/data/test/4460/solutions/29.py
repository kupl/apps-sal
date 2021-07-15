xxx = list(map(int, input().split()))
ans = 0
for i in range(5):
    if xxx[i] == 0:
        ans = i + 1
print(ans)
