n, k = (int(x) for x in input().split())

s = input()
deals = [int(x) for x in s.split()]

punish = [0 for x in range(k)]

for i in range(n):
    punish[i % k] += deals[i]

print(punish.index(min(punish)) + 1)
