
n = int(input())
a = list(map(int, input().split(' ')))
freq = {}
seen = [False for i in range(n + 1)]
ch = 0
de = []
for i in range(n):
    if a[i] not in list(freq.keys()):
        freq[a[i]] = 1
    else:
        freq[a[i]] += 1
        ch += 1

for i in range(n):
    if i + 1 not in list(freq.keys()):
        de.append(i + 1)

index = 0
for i in range(n):
    if freq[a[i]] > 1:
        if seen[a[i]] or de[index] < a[i]:
            freq[a[i]] += -1
            a[i] = de[index]
            index += 1
        else:
            seen[a[i]] = True


sol = ""
for x in a:
    sol += str(x) + " "

print(str(ch) + "\n" + sol)
