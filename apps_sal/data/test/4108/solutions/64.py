s = list(input())
t = list(input())
n = len(s)

s_par = [i for i in range(n + 1)]
t_par = [i for i in range(n + 1)]

def operation(x, par):
    for i in range(n):
        for j in range(i):
            if x[i] == x[j]:
                par[i] = par[j]
                break
    return par

if operation(s, s_par) == operation(t, t_par):
    print('Yes')
else:
    print('No')
