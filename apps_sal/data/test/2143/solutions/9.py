n = int(input())
a = list(map(int, input().split()))
cnt = [0 for i in range(2 * 10 ** 5 + 1)]
for i in range(n):
    for j in range(i + 1, n):
        cnt[a[i] + a[j]] += 1
print(max(cnt))
