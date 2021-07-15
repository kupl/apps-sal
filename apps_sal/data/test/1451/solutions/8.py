n, k = map(int, input().split())
t = list(input().split())
print(sum([(i.count('4') + i.count('7')) <= k for i in t]))
