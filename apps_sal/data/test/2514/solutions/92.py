n = int(input())
A = list(map(int, input().split()))
q = int(input())
query = [tuple(map(int, input().split())) for _ in range(q)]

s = sum(A)

B = [0 for _ in range(10**5 + 1)]
for a in A:
    B[a] += 1

for b, c in query:
    s -= b * B[b]
    s += c * B[b]
    print(s)
    B[c] += B[b]
    B[b] = 0
