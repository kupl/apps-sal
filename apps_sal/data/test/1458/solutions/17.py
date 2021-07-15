n = int(input())
S = input()
mim = ord(S[0])
IN = 1
for i in range(n - 1):
    if IN and ord(S[i]) > ord(S[i + 1]):
        print('YES') 
        print(i + 1, i + 2)
        IN = 0
if IN:
    print('NO') 

