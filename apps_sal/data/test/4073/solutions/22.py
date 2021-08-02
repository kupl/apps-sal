input()
l = list(map(int, input().split()))
x = max(l) ^ l[-1]
print(x)
