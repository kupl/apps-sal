n = int(input())

xs = list(map(int, input().split()))
if len(set(x % 2 for x in xs)) != 1:
    xs.sort()

print(' '.join(map(str, xs)))
