t = int(input())

ans = []
for i in range(t):
    n, k, d = map(int, input().split())
    days = list(map(int, input().split()))
    add = float("inf")

    for j in range(d, n + 1):
        add = min(add, len(list(set(days[j - d:j]))))

    ans.append(add)

print(*ans, sep='\n')
