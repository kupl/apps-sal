kai = input()
num = len(kai)

ans = 0

n1 = int((num - 1) / 2)

for i in range(n1):
    if kai[i] != kai[-1 * (i + 1)]:
        ans += 1

l1 = kai[0:n1]

for i in range(len(l1)):
    if l1[i] != l1[-1 * (i + 1)]:
        ans += 1

l2 = kai[n1 + 1:]

for i in range(len(l2)):
    if l2[i] != l2[-1 * (i + 1)]:
        ans += 1

if ans == 0:
    print("Yes")

else:
    print("No")
