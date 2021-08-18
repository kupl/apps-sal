n = int(input())


def change(x):
    for i in range(26):
        if x == i:
            return "abcdefghijklmnopqrstuvwxyz"[i]


r = []

while n >= 1:
    n = n - 1
    r.append(change(n % 26))
    n = n // 26

s = len(r)

for i in range(s):
    print(r[s - 1 - i], end='')
