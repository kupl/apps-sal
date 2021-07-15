n = int(input())
k = int(input())
x = list(map(int, input().split()))

print(sum([min(position, abs(k - position)) * 2 for position in x]))
