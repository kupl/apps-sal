a = int(input())
f = list(map(int, input().split()))
ans = [f[0], f[-1]]
for i in range(a - 2):
    ans.append(min(f[i], f[i + 1]))

print(sum(ans))
