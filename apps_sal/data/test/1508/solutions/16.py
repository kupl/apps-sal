input()
a = sorted(input().split(), key=int)
print(a[-1], ' '.join(a[1:-1]), a[0])

