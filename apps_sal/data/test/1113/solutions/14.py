n = input()

A = list(map(int, input().split(" ")))

max_seen = -1

for ix, a in enumerate(A):

    if a > max_seen + 1:
        print(ix + 1)
        return

    max_seen = max(max_seen, a)
print(-1)
