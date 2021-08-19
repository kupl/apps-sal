(a, b, k) = list(map(int, input().split()))
ans = []
for i in range(1, 101):
    if a % i == 0:
        if b % i == 0:
            ans.append(i)
ans = sorted(ans)
print(ans[-k])
