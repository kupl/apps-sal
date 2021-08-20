(n, n1, n2) = map(int, input().split())
l = sorted(list(map(int, input().split())))[::-1]
a = min(n1, n2)
print(sum(l[0:a]) / a + sum(l[a:n1 + n2]) / max(n1, n2))
