k, n = map(int, input().split())
alst = list(map(int, input().split()))
alst.append(alst[0] + k)
minus = 0
for i in range(n):
  minus = max(minus, alst[i + 1] - alst[i])
print(k - minus)
