n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
ans1 = []
for i in range(n):
    ans = -10 ** 18 - 1
    for j in range(n):
        if j != i:
            for q in range(m):
                if ans < l1[j] * l2[q]:
                    ans = l1[j] * l2[q]
    ans1.append(ans)
print(min(ans1))
