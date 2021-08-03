n = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in range(n - 2):
    pi = sorted(p[i:i + 3])
    if p[i + 1] == pi[1]:
        cnt += 1
print(cnt)
