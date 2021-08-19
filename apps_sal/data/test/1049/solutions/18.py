(n, d) = map(int, input().split())
c = 0
maxc = 0
while d > 0:
    x = input()
    if x.count('1') == len(x):
        maxc = max(maxc, c)
        c = 0
    else:
        c += 1
    d -= 1
maxc = max(maxc, c)
print(maxc)
