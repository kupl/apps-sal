n = int(input())
a = [int(x) for x in input().split()]
rot = input()
stack = []
pairs = []
for i in range(len(rot)):
    if rot[i] == '1' and stack == []:
        stack.append(i)
    if rot[i] == '0' and len(stack) > 0:
        stack.append(i - 1)
        pairs.append((stack[-2], stack[-1] + 1))
        stack.clear()
if len(stack) > 0:
    pairs.append((stack[-1], n))
for (l, r) in pairs:
    a[l:r + 1] = sorted(a[l:r + 1])
print('YNEOS'[not a == sorted(a)::2])
