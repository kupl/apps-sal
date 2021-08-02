good_results = set()
n = int(input())
r = list(map(int, input().split()))
for c in r:
    if c != 0:
        good_results.add(c)
print(len(good_results))
