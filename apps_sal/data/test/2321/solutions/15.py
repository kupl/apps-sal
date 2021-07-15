t = int(input())

for test in range(0,t):

    n = int(input())
    s = input()

    prefix_len=0
    suffix_len=0

    for i in range(0,n):

        ##print(i)

        if s[i]=='<':
            prefix_len+=1

        else:
            break

    for i in range(n-1,-1,-1):

        ##print(i)

        if s[i]=='>':
            suffix_len+=1

        else:
            break

    print(min(suffix_len,prefix_len))

