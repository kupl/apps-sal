N = int(input())
ans = 0

for i in range(1, N + 1):
    if len(str(i)) == 1 or len(str(i)) == 3 or len(str(i)) == 5:
        ans += 1

print(ans)
