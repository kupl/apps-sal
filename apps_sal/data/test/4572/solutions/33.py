A = [0 for i in range(26)]
S = input()
for s in S:
    A[ord(s) - 97] = 1
flag = False
for i in range(26):
    if A[i] == 0:
        flag = True
        break
if flag:
    print(chr(97 + i))
else:
    print('None')
