import math

[a, t_a] = map(int,input().split(" "))
[b, t_b] = map(int,input().split(" "))
[h, m] = map(int,input().split(":"))
mm = h * 60 + m

first_bus = 5*60
start = max(first_bus, mm - t_b + 1) - first_bus
end = min(60*23+59, mm + t_a - 1) - first_bus

# print(start, end)
# print(math.ceil(start/b), int(end/b))
print(int(end/b) - math.ceil(start/b) + 1)
