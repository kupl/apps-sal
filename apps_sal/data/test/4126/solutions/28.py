S = input()
N = len(S)

ret = 'Yes'
for s1, s2 in list(zip(S, reversed(S)))[:N//2]:
    if s1 != s2:
        ret = 'No'
        break
s = S[:N//2]
for s3, s4 in list(zip(s, reversed(s)))[:N//4]:
    if s3 != s4:
        ret = 'No'
        break

print(ret)


