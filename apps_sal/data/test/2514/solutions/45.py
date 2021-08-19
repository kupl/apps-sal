N = int(input())
A = [int(i) for i in input().split()]
Q = int(input())
d = [0] * 10 ** 5
for i in A:
    d[i - 1] += 1
ans = sum(A)
for i in range(Q):
    (b, c) = map(int, input().split())
    ans += (c - b) * d[b - 1]
    d[c - 1] += d[b - 1]
    d[b - 1] = 0
    print(ans)
