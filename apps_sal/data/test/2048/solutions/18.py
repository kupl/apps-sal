n = int(input())
s = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
cost = min((min([30000000000.0] + [c[j] for j in range(i) if s[j] < s[i]]) + c[i] + min([30000000000.0] + [c[k] for k in range(i + 1, n) if s[k] > s[i]]) for i in range(n)))
if cost >= 30000000000.0:
    cost = -1
print(cost)
