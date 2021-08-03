N = int(input())
A = list(map(int, input().split()))
tmp = 0
lr = [0]
for a in A:
    tmp += a
    lr.append(tmp)

ans = float('inf')

f, g = 1, 3
for i in range(2, N - 1):
    while abs(lr[i] - lr[f] - lr[f]) > abs(lr[i] - lr[f + 1] - lr[f + 1]):
        f += 1
    while abs((lr[-1] - lr[g]) - (lr[g] - lr[i])) > abs((lr[-1] - lr[g + 1]) - (lr[g + 1] - lr[i])):
        g += 1
    l = (lr[f], lr[i] - lr[f], lr[-1] - lr[g], lr[g] - lr[i])
    ans = min(ans, max(l) - min(l))

print(ans)
