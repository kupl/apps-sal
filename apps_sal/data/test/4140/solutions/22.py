S = input()
count = 0

for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == '0':
            count += 1
    else:
        if S[i] == '1':
            count += 1

print((min(len(S) - count, count)))

