N, K = map(int, input().split())
l = list(sorted(map(int, input().split())))[::-1]

print(sum(l[:K]))
