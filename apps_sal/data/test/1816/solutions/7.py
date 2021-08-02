n = int(input())
index = [0 for i in range(n + 1)]
a = list(map(int, input().split()))
for i in range(n):
    index[a[i]] = i

ans = 0
lab = 1
while lab != n:
    ans += abs(index[lab] - index[lab + 1])
    lab += 1

print(ans)
