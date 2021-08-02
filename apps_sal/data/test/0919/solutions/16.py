n, k = [int(c) for c in input().split(" ")]
line = [c for c in input()]
line.sort()

# print(line)

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_weight = {}
for i in range(len(alphabet)):
    alphabet_weight[alphabet[i]] = i + 1

s = 0
p = 0
i = 0
previous_weight = -10000
while i < n:
    if alphabet_weight[line[i]] > previous_weight + 1:
        s += alphabet_weight[line[i]]
        previous_weight = alphabet_weight[line[i]]
        p += 1
    if p == k:
        break
    i += 1

if i == n:
    s = -1
print(s)
