a = sorted(list(map(int, input().split())))

print((a[-1] * 10 + sum(a[:-1])))
