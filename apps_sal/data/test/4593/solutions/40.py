N = int(input())
ans = 0
for i in range(1, N + 1):
    for j in range(2, 20):
        if i ** j > N:
            continue
        ans = max(i ** j, ans)
print(ans)
