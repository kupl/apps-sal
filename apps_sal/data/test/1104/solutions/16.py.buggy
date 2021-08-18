

size: int = int(input())

seq1 = []
seq2 = []

for i in input().split(" "):
    seq1.append(int(i))

for i in input().split(" "):
    seq2.append(int(i))

out = []
for i in range(0, size):
    out.append(-1)

for tFirst in range(0, 4):
    out[0] = tFirst
    for i in range(0, size - 1):
        for t2 in range(0, 4):
            if out[i] | t2 == seq1[i] and out[i] & t2 == seq2[i]:
                out[i + 1] = t2

    if -1 not in out:
        print("YES")
        for i in out:
            print(i, end=" ")

        return

if -1 in out:
    print("NO")
