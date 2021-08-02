S = input()

for i in range(1, len(S)):
    s = S[0:len(S) - i]
    # print(s)
    if len(s) % 2 == 1:
        continue
    #print('pre', s[0:int(len(s)/2)+1])
    #print('follow', s[int(len(s)/2):len(s)])
    if s[0:int(len(s) / 2)] == s[int(len(s) / 2):len(s)]:
        print(len(S) - i)
        break
