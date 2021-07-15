N = int(input())
s = input()
inv = {'S':'W','W':'S'}

prefix = ['SS','SW','WS','WW']

def check_i(i): # check0,check-1だけすれば十分
    if s[i] == 'o' and ans[i] == 'S':
        if ans[i+1] != ans[i-1]:
            return False
    if s[i] == 'x' and ans[i] == 'S':
        if ans[i+1] == ans[i-1]:
            return False
    if s[i] == 'o' and ans[i] == 'W':
        if ans[i+1] == ans[i-1]:
            return False
    if s[i] == 'x' and ans[i] == 'W':
        if ans[i+1] != ans[i-1]:
            return False
    return True


for p in prefix:
    ans = p
    for i in range(1,N-1):
        if s[i] == 'o' and ans[i] == 'S':
            ans += ans[i-1]
        if s[i] == 'x' and ans[i] == 'S':
            ans += inv[ans[i-1]]
        if s[i] == 'o' and ans[i] == 'W':
            ans += inv[ans[i-1]]
        if s[i] == 'x' and ans[i] == 'W':
            ans += ans[i-1]
    if check_i(0) and check_i(-1):
        print(ans)
        return
print((-1))



