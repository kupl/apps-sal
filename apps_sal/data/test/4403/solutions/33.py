S = list(input())
count = 0
for i in range(4):
    if S[i] == '+':
        count = count + 1
    elif S[i] == '-':
        count = count - 1
print(count)
