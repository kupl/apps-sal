N = int(input())
a = list(map(int, input().split()))
Q = [0] * (max(a) + 3)
for i in a:
    Q[i] += 1
    Q[i + 1] += 1
    Q[i + 2] += 1
print(max(Q))
