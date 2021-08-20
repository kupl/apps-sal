n = int(input())
MODULO = 10 ** 9 + 7
i = 0
dp = [[0 for i in range(n + 2)] for j in range(n + 2)]
dp[0][0] = 1
new_array = [0] * (n + 2)
old_array = [0] * (n + 2)
new_array[0] = 1
for i in range(n):
    c = input()[0]
    old_array = new_array
    new_array = [0] * (n + 2)
    if c == 'f':
        for j in range(n):
            new_array[j + 1] = old_array[j]
    else:
        j = i + 1
        tmp = 0
        while j >= 0:
            tmp = (tmp + old_array[j]) % MODULO
            new_array[j] = tmp % MODULO
            j -= 1
tmp = 0
for i in range(n):
    tmp = (tmp + old_array[i]) % MODULO
print(tmp)
