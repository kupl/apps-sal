import sys
sys.setrecursionlimit(10**9)

s = input()
l = len(s)


def dfs(i):
   #    print("->", s[i:])
    if i == l:
        print("YES")
        return
    if s[i:i+5] == "dream":
        if i+6 < l and s[i+5:i+7] == "er":
            dfs(i+7)
        dfs(i+5)
    elif s[i:i+5] == "erase":
        if i+5 < l and s[i+5] == "r":
            dfs(i+6)
        dfs(i+5)


dfs(0)
print("NO")

