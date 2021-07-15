S = input()

l = len(S)

l = (l-2)//2
while l > 0:
    if S[0:l] == S[l:2*l]:
        print((2*l))
        break
    l = l-1

