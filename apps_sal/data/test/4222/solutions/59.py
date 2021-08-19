(n, k) = map(int, input().split())
d = []
a = []
for i in range(k):
    d.append(int(input()))
    a.append(list(map(int, input().split())))
cnt = 0
for i in range(1, n + 1):
    if i not in set(sum(a, [])):
        cnt += 1
print(cnt)
