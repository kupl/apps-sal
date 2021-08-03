S = input()
sum = 0
for i in range(len(S)):
    if S[i] == '+':
        sum += 1
    else:
        sum -= 1
print(sum)
