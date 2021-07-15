input()
a = list(map(int, input().split()))
tl = max(2 * min(a), max(a))
if tl < min(list(map(int, input().split()))):
    print(tl)
else:
    print(-1)

