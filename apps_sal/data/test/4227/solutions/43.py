import itertools
n, m = list(map(int, input().split()))
num = [[] for _ in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    num[a - 1].append(b)
    num[b - 1].append(a)
cnt = list(itertools.permutations(list(range(2, n + 1))))
ans = 0
for i in range(len(cnt)):
    num1 = 1
    num2 = cnt[i]
    yn = 0
    for j in range(n - 1):
        if num2[j] not in num[num1 - 1]:
            yn = 1
            break
        num1 = num2[j]
    if yn == 0:
        ans += 1
print(ans)
