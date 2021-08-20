import sys
input = sys.stdin.readlines()
n = int(input[0].strip())
m = 10 ** 9 + 7
curr = [0] * (n + 20)
last = [0] * (n + 20)
curr[0] = 1
for s in range(1, n):
    (last, curr) = (curr, last)
    if input[s] == 'f\n':
        curr[0] = 0
        for i in range(len(last) - 1):
            curr[i + 1] = last[i]
    elif input[s] == 's\n':
        curr[-1] = 0
        for i in range(len(last) - 2, -1, -1):
            curr[i] = (curr[i + 1] + last[i]) % m
s = 0
for x in curr:
    s = (s + x) % m
print(s)
