n = input()
l = sorted(map(int, input().split()))
m = sum(l[:-1])
print(l[-1] + 1 - m)
