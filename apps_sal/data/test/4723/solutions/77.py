s = list(input())
t = list(input())
ls =len(s)
lt = len(t)
s.reverse()
t.reverse()
for i in range(ls):
    for j in range(lt):
        if i + j >= ls:
            break
        if s[i+j] != '?' and s[i+j] != t[j]:
            break
    else:
        for j in range(lt):
            s[i+j] = t[j]
        s = [x if x != '?' else 'a' for x in s]
        s.reverse()
        ans = ''.join(s)
        break
else:
    ans = 'UNRESTORABLE'
print(ans)
