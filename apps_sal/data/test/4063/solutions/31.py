N = int(input())
a = list(map(int, input().split()))
a.sort()
half = int(len(a) / 2)
if a[half - 1] == a[half]:
    print(0)
else:
    print(a[half] - a[half - 1])
