alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
mapping = [0] * 10
n = int(input())
firstLetter = []
for i in range(n):
    s = input()
    firstLetter.append(s[0])
    for j in range(len(s)):
        mapping[alphabets.index(s[j])] += 10 ** (len(s) - j - 1)
flow = 1
catchZero = 0
ans = 0
for i in range(10):
    saikyu = 0
    for j in range(10):
        if saikyu < mapping[j]:
            saikyu = mapping[j]
    if alphabets[mapping.index(saikyu)] not in firstLetter and catchZero == 0:
        catchZero = 1
    else:
        ans += saikyu * flow
        flow += 1
    mapping[mapping.index(saikyu)] = 0
print(ans)
