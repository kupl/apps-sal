x = list(map(int, input().split()))

ans = 0

for i in range(5):
    if x[i] == 0:
        ans = i + 1

print(ans)
