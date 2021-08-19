S = input()
even = []
odd = []
for i in range(len(S)):
    if i % 2 == 0:
        even.append(S[i])
    else:
        odd.append(S[i])
if 'L' not in even and 'R' not in odd:
    print('Yes')
else:
    print('No')
