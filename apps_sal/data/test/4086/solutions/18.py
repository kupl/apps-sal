l = int(input())
n = input().split()
revert = n[::-1]
out = []
for x in range(l):
    i = revert[x]
    if i in out:
        continue
    out.append(i)
print(len(out))
print(' '.join(out[::-1]))
