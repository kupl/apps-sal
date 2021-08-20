N = int(input())
n = list(map(int, input().split()))
cnt = 0
for i in range(N - 2):
    if max(n[0 + i], n[1 + i], n[2 + i]) > n[1 + i] > min(n[0 + i], n[1 + i], n[2 + i]):
        cnt += 1
print(cnt)
