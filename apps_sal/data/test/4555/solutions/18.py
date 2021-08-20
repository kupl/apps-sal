(a, b, k) = map(int, input().split())
l = [i for i in range(a, min(b, a + k))]
l = l + [i for i in range(max(a, b - k + 1), b + 1)]
l = list(set(l))
l.sort()
for i in l:
    print(i)
