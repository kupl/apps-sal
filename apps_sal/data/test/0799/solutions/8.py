s = input()
s = list(map(int, input().split()))
print(len(s) * max(s) - sum(s))
