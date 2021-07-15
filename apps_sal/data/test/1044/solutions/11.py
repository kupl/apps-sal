n = int(input())
data = list(map(int, input().split()))
for i in range(n):
    data[i] -= 1
winner = data[0] % 2
print(2 - winner)
for i in range(1, n):
    if data[i] % 2 == 1:
        winner ^= 1
    print(2 - winner)
