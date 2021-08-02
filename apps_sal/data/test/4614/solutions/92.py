s = list(map(int, input().split()))
i = set(s)
print(sum(i) - (sum(s) - sum(i)))
