n, k = map(int, input().split())
p = list(map(int, input().split()))
li = [sum(p[0:k])]
for i in range(n - k):
    li.append(li[i] - p[i] + p[i + k])
print((max(li) + k) / 2)
