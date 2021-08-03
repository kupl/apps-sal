import itertools

n = int(input())
town = [list(map(int, input().split())) for _ in range(n)]
x = 1
for i in range(1, n + 1):
    x *= i
l = []
for j in range(n):
    l.append(j)
ans = 0
for a in itertools.permutations(l, n):
    newl = a
    length = 0
    for b in range(n - 1):
        length += ((town[newl[b]][0] - town[newl[b + 1]][0])**2 + (town[newl[b]][1] - town[newl[b + 1]][1])**2)**(1 / 2)
    ans += length
print(ans / x)
