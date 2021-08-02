import sys

input = sys.stdin.readline

n = int(input())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

perm = [-1 for i in range(n)]
avail = set()

for i in range(1, n + 1):
    avail.add(i)

for i in range(n):
    if a[i] == b[i]:
        avail.remove(a[i])
        perm[i] = a[i]


def difference(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
        if count > 1:
            return 0
    return 1


def solve(seq, curravail):
    if not curravail:
        if difference(seq, a) == 1 and difference(seq, b) == 1:
            return seq
    for i in range(len(seq)):
        if (seq[i] == -1):
            for item in list(curravail):
                newseq = list(seq)
                newseq[i] = item
                newset = set(curravail)
                newset.remove(item)
                if solve(newseq, newset):
                    return solve(newseq, newset)


print(" ".join(map(str, solve(perm, avail))))
