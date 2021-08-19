import sys
sys.setrecursionlimit(4100000)
N = int(input())
mod = 10 ** 9 + 7
L = [{} for i in range(101)]


def check(txt):
    if 'AGC' in txt:
        return False
    List = list(txt)
    for i in range(3):
        (List[i], List[i + 1]) = (List[i + 1], List[i])
        if 'AGC' in ''.join(List):
            return False
        (List[i], List[i + 1]) = (List[i + 1], List[i])
    return True


def dfs(i, txt):
    if i == N:
        return 1
    if txt in L[i]:
        return L[i][txt]
    ans = 0
    for char in 'AGCT':
        if check(txt[1:] + char):
            ans += dfs(i + 1, txt[1:] + char)
    L[i][txt] = ans % mod
    return ans % mod


print(dfs(0, 'TTTT'))
