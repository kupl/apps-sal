s = input()
K = int(input())

seq = set()
l = len(s)
for i in range(l):
    for j in range(1, K + 1):
        seq.add(s[i:i + j])

seq = list(seq)
seq.sort()
print((seq[K - 1]))

