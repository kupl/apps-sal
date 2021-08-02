a = input()
b = input()
cntr = 0
curr = min(len(a), len(b)) - 1
for i in range(1, min(len(a), len(b)) + 1, 1):
    if a[-i] == b[-i]:
        cntr += 1
    else:
        break
print(len(a) - cntr + len(b) - cntr)
