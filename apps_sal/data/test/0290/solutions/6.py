n = int(input())
ans = []
for i in range(1, 100000):
    ans.append(i + (n - 1) // i + 1)
print(min(ans))
