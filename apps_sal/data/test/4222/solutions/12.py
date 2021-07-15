n, k = map(int, input().split())
s = [0] * n

for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for x in a:
        s[x-1] = 1

print(s.count(0))
