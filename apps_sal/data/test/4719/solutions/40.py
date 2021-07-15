a = ord('a')
n = int(input())
memory = [[0] * 26 for _ in range(n)]

for i in range(n):
    for s in input():
        memory[i][ord(s) - a] += 1

ans = ''
for i in range(26):
    ans += min(memory[j][i] for j in range(n)) * chr(a + i)

print(ans)
