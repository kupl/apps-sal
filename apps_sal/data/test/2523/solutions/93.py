S = input()
length = len(S)
temp = []
for i in range(1, length):
    if S[i] != S[i - 1]:
        temp.append(max(i, length - i))
if len(temp) == 0:
    print(length)
else:
    print(min(temp))
