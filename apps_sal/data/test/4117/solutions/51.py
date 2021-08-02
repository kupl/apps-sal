n = int(input())

l_n = list(map(int, input().split()))
l_n.sort()

ans = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if l_n[i] != l_n[j] != l_n[k] and l_n[i] + l_n[j] > l_n[k]:
                ans += 1

print(ans)
