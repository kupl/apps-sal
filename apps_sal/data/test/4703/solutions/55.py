def dfs(i,sall):
    if i == lenS:
        return (sall)
        #return sum(map(int,(s[0]+sall).split("+")))
    return dfs(i + 1,sall+"+"+s[i])+"+"+dfs(i + 1,sall+s[i])

s = input()
lenS = len(s)
print(sum(map(int,dfs(1,s[0]).split("+"))))
