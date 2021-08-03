n = int(input())
food = list(map(int, input().split()))
times = {}
for i in range(n):
    times[food[i]] = i
t = min(times.values())
print(food[t])
