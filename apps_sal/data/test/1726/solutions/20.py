n, t = [int(i) for i in input().split()]

a = [int(i) for i in input().split()]

ans = 1
sums = []

for i in a:
    sums.append(86400 - i)

while sum(sums[0:ans]) < t:
    ans += 1

print(ans)
