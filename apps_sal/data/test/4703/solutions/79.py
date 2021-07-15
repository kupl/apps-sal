S = input()
n = len(S)-1
result = 0
for i in range(2 ** n):
    sum = 0
    temp = ''
    for j in range(n):
        temp += S[j]
        if (i >> j) & 1:
            sum += int(temp)
            temp = ''
    sum += int(temp+S[-1])
    result += sum
print(result)
