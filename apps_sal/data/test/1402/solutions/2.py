from functools import reduce

n = int(input())

s1, s2 = str(input()), str(input())

b1 = reduce(lambda x, y: x or y, [s1[i] != '?' and s2[i] != '?' and ord(s1[i]) < ord(s2[i]) for i in range(n)], False)

b2 = reduce(lambda x, y: x or y, [s1[i] != '?' and s2[i] != '?' and ord(s1[i]) > ord(s2[i]) for i in range(n)], False)

s = sum([(s1[i] == '?') + (s2[i] == '?') for i in range(n)])

ans1 = reduce(lambda x, y: (x * y) % 1000000007, [55 if s1[i] == '?' and s2[i] == '?' else (ord(s2[i]) - ord('0') + 1) if s1[i] == '?' else (10 - ord(s1[i]) + ord('0')) if s2[i] == '?' else 1 for i in range(n)], 1)

ans2 = reduce(lambda x, y: (x * y) % 1000000007, [55 if s1[i] == '?' and s2[i] == '?' else (10 - ord(s2[i]) + ord('0')) if s1[i] == '?' else (ord(s1[i]) - ord('0')) + 1 if s2[i] == '?' else 1 for i in range(n)], 1)

ans3 = reduce(lambda x, y: (x * y) % 1000000007, [10 if s1[i] == '?' and s2[i] == '?' else 1 for i in range(n)], 1)

print((10 ** s - (not b2) * ans1 - (not b1) * ans2 + (not b1 and not b2) * ans3) % 1000000007)
