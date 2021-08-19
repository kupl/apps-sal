n = int(input())
fact = [0, 1]
for i in range(2, n + 1):
    fact.append(fact[-1] * i % 998244353)
ans = [0, 1]
for i in range(2, n + 1):
    ans.append((fact[i] + i * ans[-1] - i) % 998244353)
print(ans[-1])
