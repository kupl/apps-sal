input()
l = list(map(int, input().split()))
l = sorted(l)
print(sum(l[::2]))
