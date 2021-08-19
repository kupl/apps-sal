import math

N, r = list(map(int, input().split()))

# sin(360/N)=R/(r+R)

print(r * math.sin(math.pi / N) / (1 - math.sin(math.pi / N)))
# print(math.sin(math.pi/N))
