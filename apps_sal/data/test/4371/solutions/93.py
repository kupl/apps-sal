s = list(input())
m = 642
for i in range(len(s) - 2):
    if abs(100 * int(s[i]) + 10 * int(s[i + 1]) + int(s[i + 2]) - 753) < m:
        m = abs(100 * int(s[i]) + 10 * int(s[i + 1]) + int(s[i + 2]) - 753)

print(m)
