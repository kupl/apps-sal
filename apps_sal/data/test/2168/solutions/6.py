n = int(input())
a = [list(map(int, input().split()))[1:] for q in range(n)]
max1 = [max(q) for q in a]
max_max = max(max1)
answer = 0
for q in range(n):
    answer += (max_max - max1[q]) * len(a[q])
print(answer)
