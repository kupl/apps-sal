n = int(input())
A = list(map(int, input().split()))
sum_a = sum(A)
d = dict()
for a in A:
    d[a] = d.get(a, 0) + 1
for _ in range(int(input())):
    (b, c) = list(map(int, input().split()))
    if d.get(b, 0) != 0:
        temp = d[b]
        d[b] -= temp
        d[c] = d.get(c, 0) + temp
        sum_a += (c - b) * temp
    print(sum_a)
