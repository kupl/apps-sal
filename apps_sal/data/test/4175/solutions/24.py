N = int(input())
l = []
l.append(input())
ans = 'Yes'

for i in range(1, N):
    t = input()
    if t in l:
        ans = 'No'
        break
    elif l[i - 1][-1] == t[0]:
        l.append(t)
    else:
        ans = 'No'
        break
print(ans)
