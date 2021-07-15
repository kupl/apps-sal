n = int(input())
H1 = list(map(int, input().split()))
H2 = list(map(int, input().split()))
av = list(map(int, input().split()))
ans = []
for i in range(n - 1):
    ans.append(sum(H1[:i]) + av[i] + sum(H2[i:]))
ans.append(sum(H1) + av[-1])
ans.sort()
print(ans[0] + ans[1])

