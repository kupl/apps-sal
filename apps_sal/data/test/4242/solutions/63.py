(a, b, k) = map(int, input().split())
ans = []
for i in range(1, a + 1):
    for j in range(1, b + 1):
        if i == j and a % i == 0 and (b % j == 0):
            ans.append(i)
print(ans[-k])
