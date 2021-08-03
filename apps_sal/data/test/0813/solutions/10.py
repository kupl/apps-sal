n, a, b = map(int, input().split())
otv = [2] * 101
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s1 = sorted(s1)
s2 = sorted(s2)
for i in range(a):
    otv[s1[i]] = 1
for i in range(1, n + 1):
    print(otv[i], end=' ')
