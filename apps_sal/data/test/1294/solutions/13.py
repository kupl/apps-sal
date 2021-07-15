T = int(input())

for _ in range(T):
    X = [0] * 26
    s = input()
    while s:
        if len(s) == 1:
            X[ord(s[0])-97] = 1
            break
        if s[0] == s[1]:
            s = s[2:]
        else:
            X[ord(s[0])-97] = 1
            s = s[1:]
    
    print("".join([chr(97+i) for i in range(26) if X[i]]))


