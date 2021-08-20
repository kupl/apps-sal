n = int(input())
s = [int(x) for x in input()]
print(''.join(map(str, min([[(x + 10 - s[j]) % 10 for x in s[j:] + s[:j]] for j in range(n)]))))
