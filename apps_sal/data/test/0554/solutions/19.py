(n, m) = list(map(int, input().split()))
d = list(map(int, input().split()))
answer = 0
for i in range(m):
    (i, j) = list(map(int, input().split()))
    i -= 1
    t = sum(d[i:j])
    if t > 0:
        answer += t
print(answer)
