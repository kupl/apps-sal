n = list(input())
k = set()
for i in range(len(n) + 2):
    for j in range(26):
        k.add(''.join(str(n[:i] + [chr(j + 97)] + n[i:])))
print(len(k))
