s = list(input())
t = list(input())
ls, lt = len(s), len(t)
#リストを反転させてケツから調べる事で辞書順最小を求める
s.reverse()
t.reverse()
for i in range(ls):
    for j in range(lt): #このfor文が全部回ればt in sである
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
