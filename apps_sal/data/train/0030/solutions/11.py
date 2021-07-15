t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    S = 0
    for j in range(1,len(s)):
        if s[j-1]=='1' and s[j]=='1':
            S+=1
    if s[0]=='1' and s[-1]=='1' and len(s)>2:
        S+=1
    print(S)

