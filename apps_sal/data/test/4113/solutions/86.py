N = int(input())
ans = 'No'
for d in range(N // 7 + 1):
    if (N - 7 * d) % 4 == 0:
        ans = 'Yes'
        break
print(ans)
