n = int(input())
s = input()
s = [int(x) for x in s]
print("".join(map(str, min([[(x + 10 - s[j]) % 10 for x in (s[j:] + s[:j])] for j in range(n)]))))
