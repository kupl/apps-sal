st1 = input()
st2 = input()
l1 = len(st1)
l2 = len(st2)
i = l1 - 1
j = l2 - 1
while (st1[i] == st2[j]):
    i -= 1
    j -= 1
    if (i < 0) or (j < 0):
        break

print(i + j + 2)
