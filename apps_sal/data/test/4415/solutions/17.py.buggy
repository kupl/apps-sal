from collections import Counter
n = int(input())
l = [int(i) for i in input().split()]
l.sort()
c = Counter(l)
if any(c[i] > 2 for i in c):
    print('NO')
    return
seq1 = []
seq2 = []
for i in sorted(set(l)):
    if c[i] == 1:
        seq1.append(i)
    else:
        seq1.append(i)
        seq2.append(i)
print('YES')
print(len(seq1))
print(*seq1)
print(len(seq2))
seq2 = seq2[::-1]
print(*seq2)
