S = list(input())
L = len(S)
Slist = set()
for i in range(L):
    Slist.add(ord(S[i]))
Slist = list(Slist)
Slist.sort()
ans = "None"
j = 0
L = len(Slist)
for i in range(97, 123):
    if Slist[j] == i:
        j += 1
        if j >= L and i + 1 < 123:
            ans = chr(i + 1)
            break
        continue
    ans = chr(i)
    break
print(ans)
