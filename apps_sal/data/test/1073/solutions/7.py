n = int(input())
s = input()
result = 0
for start in range(n):
    for finish in range(start + 1, n + 1):
        tmp = s[start:finish]
        if tmp.count('U') == tmp.count('D') and tmp.count('L') == tmp.count('R'):
            result += 1
print(result)
