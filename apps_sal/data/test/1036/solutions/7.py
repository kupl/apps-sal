n, k = map(int, input().split())
s = list(input())

judge_d = [
    [0, 0, 2], 
    [0, 1, 1], 
    [2, 1, 2],
]
name_to_ind = {'R':0, 'S':1, 'P':2}
ind_to_name = ['R', 'S', 'P']

def judge(a, b):
    a, b = name_to_ind[a], name_to_ind[b]
    ind = judge_d[a][b]
    return ind_to_name[ind]

def Rec(s, k):
    if k == 1:
        if len(s) == 1:
            s = s + s
        print(judge(s[0], s[1]))
    else:
        if len(s) % 2 == 1:
            s = s + s
        l = len(s) // 2
        S = []
        for i in range(l):
            S.append(judge(s[i*2], s[i*2+1]))
        Rec(S, k-1)

Rec(s, k)
