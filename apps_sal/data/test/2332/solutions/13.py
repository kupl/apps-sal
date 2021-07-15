n, k, m = list(map(int, input().split()))
w = input().split()
a = list(map(int, input().split()))
d = dict(list(zip(w, a)))

for i in range(k):
    s = list(map(int, input().split()[1:]))

    m = min(d[w[x-1]] for x in s)
    for x in s:
        d[w[x-1]] = m

print(sum(d[x] for x in input().split()))

