n, k = list(map(int, input().split()))
a = []
for i in range(k):
    d = int(input())
    ai = list(map(int, input().split()))
    for j in range(d):
        if not (ai[j] in a):
            a.append(ai[j])

print((n - len(a)))

