n = int(input())
a = list(map(int, input().split()))
s = [0]
for v in a:
    s.append(s[-1] + v)
q = int(input())
for _ in range(q):
    (l, r) = list(map(int, input().split()))
    print((s[r] - s[l - 1]) // 10)
