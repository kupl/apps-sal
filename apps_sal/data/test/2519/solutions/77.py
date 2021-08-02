N, K = map(int, input().split())
p = list(map(int, input().split()))
l = [sum(p[:K])]
# return
for i in range(1, N - K + 1):
    l.append(l[-1] - p[i - 1] + p[i + K - 1])
# L=l.index(max(l))
# print(l)
print((max(l) + K) / 2)
