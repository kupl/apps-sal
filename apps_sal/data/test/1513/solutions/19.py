n,m,k = list(map(int, input().strip().split()))

b = list(map(int, input().strip().split()))

diffs = []

for j in range(len(b)-1):
    diffs.append(b[j+1] - b[j] - 1)

diffs.sort()

tape = len(b)

segmentov = len(b)
indeks = 0
while segmentov > k:
    tape += diffs[indeks]
    indeks += 1
    segmentov -= 1

print(tape)


