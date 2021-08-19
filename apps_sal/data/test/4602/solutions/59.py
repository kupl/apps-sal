N = int(input())
K = int(input())
X = list(map(int, input().split()))
cnt = 0
for x in X:
    cnt += min(x, abs(K - x)) * 2
print(cnt)
