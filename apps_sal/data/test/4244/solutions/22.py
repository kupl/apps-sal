N = int(input())
X_list = list(map(int, input().split()))
distance = 10 ** 9
min_val = min(X_list)
max_val = max(X_list)
P_list = list(range(min_val, max_val + 1))
for _ in range(N):
    for p in P_list:
        temp = 0
        for x in X_list:
            temp += (p - x) ** 2
        if temp < distance:
            distance = temp
print(distance)
