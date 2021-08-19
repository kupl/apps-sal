N = int(input())
V = list(map(int, input().split()))
while len(V) > 1:
    V = sorted(V)
    temp = (V.pop(0) + V.pop(0)) / 2
    V.append(temp)
print(V[0])
