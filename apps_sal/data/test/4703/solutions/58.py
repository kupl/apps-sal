def dfs(i, f):
    if i == n-1: #もし枝が最後のけたに到達したら、という条件式
        return sum (list(map(int, f.split('+'))))
    
    #式fの末尾に'+'を追加する/追加しないをして次の数字を追加
    return dfs(i+1, f+s[i+1]) + dfs(i+1, f+'+'+s[i+1])
s = input()
n = len(s)
print((dfs(0, s[0])))

