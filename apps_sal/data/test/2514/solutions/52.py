N = int(input())
natural = list(map(int, input().split()))
Q = int(input())
number = [0] * (10**5 + 1)
for i in range(N):
    number[natural[i]] += 1
Nsum = sum(natural)
ans = []
for i in range(Q):
    B, C = map(int, input().split())
    count = number[B]
    diff = C - B
    number[C] += count
    number[B] = 0
    Nsum += diff * count
    ans.append(Nsum)

for i in range(Q):
    print(ans[i])
