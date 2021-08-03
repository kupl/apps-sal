n, k = map(int, input().split())
a = list(input())
g = [0] * k
for i in a:
    g[ord(i) - 65] += 1
print(k * min(g))
