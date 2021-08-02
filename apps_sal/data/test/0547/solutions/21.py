n, k = [int(x) for x in input().split()]

passwords = []

for i in range(0, n):
    passwords.append(len(input()))

correct = len(input())

passwords = sorted(passwords)

t = 0
i = 0

opt, pes = -1, -1

for i in range(0, len(passwords)):
    t += 1
    if passwords[i] == correct:
        pes = t
        if opt == -1:
            opt = t
    if (i + 1) % k == 0:
        t += 5

print(opt, pes)
