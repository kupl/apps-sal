n = int(input())
P = list(map(int, input().split()))

count = 0
for i in range(1, len(P) - 1):
    p_ = [P[i - 1], P[i], P[i + 1]]
    if (P[i] != min(p_)) and (P[i] != max(p_)):
        count += 1

print(count)
