N = int(input())
l = list(map(int, input().split()))
sum_n = sum(l)
first = sum_n - 2 * sum([l[i] for i in range(1, N, 2)])
ans = [first]
for i in range(N - 1):
    ans.append(2 * l[i] - ans[-1])
print(*ans)
