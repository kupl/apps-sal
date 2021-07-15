N = int(input())
W = list(map(int,input().split()))

mae = []
ushiro = []
abso = []

x = 1
y = 0
while x < N:
    mae.append(W[:x])
    ushiro.append(W[x:])
    x += 1

while y < N - 1:
    abso.append(abs(sum(mae[y]) - sum(ushiro[y])))
    y += 1

print(min(abso))
