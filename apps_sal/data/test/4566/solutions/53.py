(n, m) = list(map(int, input().split()))
a_s = []
b_s = []
for i in range(m):
    (a, b) = list(map(int, input().split()))
    a_s.append(a)
    b_s.append(b)
for i in range(1, n + 1):
    print(a_s.count(i) + b_s.count(i))
