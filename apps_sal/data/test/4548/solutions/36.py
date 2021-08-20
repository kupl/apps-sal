(n, m, x) = map(int, input().split())
a = list(map(int, input().split()))
acc = [0] * (n + 1)
for i in a:
    acc[i] = 1
print(min(sum(acc[:x]), sum(acc[x:])))
