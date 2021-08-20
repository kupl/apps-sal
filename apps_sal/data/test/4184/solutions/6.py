N = int(input())
W = list(map(int, input().split()))
answer = 1000000
for t in range(N):
    s1 = 0
    for i in range(t + 1):
        s1 = s1 + W[i]
    s2 = 0
    for i in range(t + 1, N):
        s2 = s2 + W[i]
    d = abs(s1 - s2)
    if d < answer:
        answer = d
        bangou = t
print(answer)
