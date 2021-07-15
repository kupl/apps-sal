used = [0 for i in range(333)]
p = []
t = []
n = 0
c = []
d = []

def dfs(v):
    used[v] = 1
    c.append(v)
    d.append(p[v])
    for i in range(len(p)):
        if t[v][i] == '1' and not used[i]:
            dfs(i)
def main():
    nonlocal n
    nonlocal p
    nonlocal t
    nonlocal used
    nonlocal c
    nonlocal d
    n = int(input())
    p = [int(i) for i in input().split()]
    t = []
    ans = [0 for i in range(n)]
    for i in range(n):
        t.append(input())
    for i in range(n):
        if not used[i]:
            c = []
            d = []
            dfs(i)
            k = len(c)
            for num,val in zip(sorted(c), sorted(d)):
                ans[num] = val 
    for elem in ans:
        print(elem, end = ' ')
def __starting_point():
    main()
__starting_point()
