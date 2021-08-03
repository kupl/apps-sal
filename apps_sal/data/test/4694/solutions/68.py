N = int(input())
house = list(map(int, input().split()))

print(max(house) - min(house))
