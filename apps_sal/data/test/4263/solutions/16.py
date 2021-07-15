S = str(input())
count = 0
data = []


for i in range(len(S)):
    if (S[i] == 'A') or (S[i] == 'T') or (S[i] == 'C') or (S[i] == 'G'):
        count += 1
    else:
        data.append(count)
        count = 0

data.append(count)

print(max(data))
