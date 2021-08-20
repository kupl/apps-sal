(n, m) = map(int, input().split())
answer = [0] * n
for i in range(m):
    l = list(map(int, input().split()))
    answer[l.index(max(l))] += 1
print(answer.index(max(answer)) + 1)
