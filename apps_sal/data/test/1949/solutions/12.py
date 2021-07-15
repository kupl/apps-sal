n, k = list(map(int, input().split()))

l = list(map(int, input().split()))

s = list(set(l))

s.sort()

s = s[:k] + [0 for i in range(k)]

a = 0

for i in range(k):
    print(max(0, s[i] - a))
    a = s[i]

