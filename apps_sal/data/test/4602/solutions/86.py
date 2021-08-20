N = int(input())
K = int(input())
X = list(map(int, input().split()))
Y = [i for i in range(1, N + 1)]
ans = 0
for x in X:
    distance_a = x
    distance_b = abs(K - x)
    if distance_a < distance_b:
        ans += distance_a
    else:
        ans += distance_b
print(ans * 2)
