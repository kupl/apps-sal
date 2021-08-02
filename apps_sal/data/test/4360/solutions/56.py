N = int(input())
A = list(map(int, input().split()))
Arev = []

for a in A:
    Arev.append(1 / a)

print((1 / sum(Arev)))
