s = input().strip().replace("7", "1").replace("4", "0")
m = 0
for i in range(1, len(s)):

    m += 2 ** i

print(int(s, 2) + m + 1)

