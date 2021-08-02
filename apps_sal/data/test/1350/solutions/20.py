n, k = list(map(int, input().split()))
s = input()
g = [0] * k
for i in s:
    g[ord(i) - 65] += 1
print(k * min(g))
