S = input()
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = []
for alpha in alphabets:
    if S.count(alpha) > 0 :
        ans.append(1)
    else:
        ans.append(0)

if sum(ans) == 26:
    print('None')
else:
    print((alphabets[ans.index(0)]))

