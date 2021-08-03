n, k = map(int, input().split())
h = [0] * n
for i in range(n):
    h[i] = int(input())
h = sorted(h)
answer = 100000000000000
for j in range(n + 1 - k):
    answer = min(answer, h[j - 1 + k] - h[j])
print(answer)
