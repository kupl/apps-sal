import sys

S = sys.stdin.readline().strip()
weathers = ["Sunny", "Cloudy", "Rainy"]
print(weathers[(weathers.index(S) + 1) % 3])
