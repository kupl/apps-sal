ct = [0] * 26

n, k = [int(i) for i in input().split()]
s = input()

for i in s:
    ct[ord(i) - ord('A')] += 1

print(min(ct[:k]) * k)
