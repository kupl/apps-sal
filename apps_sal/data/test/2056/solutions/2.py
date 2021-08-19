import sys
lines = sys.stdin.readlines()
n = int(lines[0].strip())
arr = list(map(int, lines[1].strip().split(' ')))
digits = [0 for _ in range(21)]
for a in arr:
    b = bin(a)[2:]
    for i in range(1, len(b) + 1):
        if b[-i] == '1':
            digits[i - 1] += 1
final = []
for i in range(n):
    tmp = 0
    for j in range(21):
        if digits[j] != 0:
            tmp += 2 ** j
            digits[j] -= 1
    final.append(tmp)
res = 0
for num in final:
    res += num ** 2
print(res)
