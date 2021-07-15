data = input()
MOD = 10**9 + 7
SLen = len(data)
targets = "ABC"
array = [[0 for i in range(SLen + 1)] for _ in range(4)]
array[0][0] = 1
for i in range(SLen):
    for j in range(4):
        if data[i] == '?':
            if j < 3:
                array[j + 1][i + 1] = (array[j + 1][i + 1] + array[j][i]) % MOD
            array[j][i + 1] = (array[j][i + 1] + array[j][i] * 3) % MOD
        else:
            if j < 3 and data[i] == targets[j]:
                array[j + 1][i + 1] = (array[j + 1][i + 1] + array[j][i]) % MOD
            array[j][i + 1] = (array[j][i + 1] + array[j][i]) % MOD

print((array[3][SLen]))

