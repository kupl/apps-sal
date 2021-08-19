S = input()
a = [0] * 26
for i in range(len(S)):
    tmp = ord(S[i]) - ord('a')
    a[tmp] = 1
for i in range(26):
    if a[i] == 0:
        tmp = chr(ord('a') + i)
        print(tmp)
        break
else:
    print('None')
