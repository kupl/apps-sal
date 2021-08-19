N = int(input())
X = list(map(int, input().split()))
p = round(sum(X) / N)
cnt = 0
for i in X:
    cnt += (i - p) ** 2
print(cnt)
