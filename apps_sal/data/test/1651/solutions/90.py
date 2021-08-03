import math


s, p = list(map(int, input().split()))
max_range = math.sqrt(10 ** 13)
for i in range(int(max_range)):
    if i * (s - i) == p:
        print("Yes")
        return
print("No")
