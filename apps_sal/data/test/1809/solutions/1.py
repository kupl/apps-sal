"""
Codeforces Contest Good Bye 2014 Contest Problem C

Author  : chaotic_iak
Language: Python 3.4.2
"""

################################################### SOLUTION

def main():
    n,m = read()
    w = read()
    b = read()
    bookset = set(range(1,n+1))
    print(solve(b, w, bookset, n))

def solve(b, w, bookset, n):
    if len(b) <= 1: return 0
    used = [0] * (n+1)
    sm = 0
    for i in range(len(b)):
        if not used[b[i]]:
            sm += 1
        if sm == len(bookset):
            res = solve(b[:i], w, bookset - {b[i]}, n)
            for j in range(i, len(b)):
                for k in range(n+1):
                    if used[k] > used[b[j]]: res += w[k-1]
                used[b[j]] = j+1
            return res
        used[b[i]] = i+1
    bookset = set(filter(lambda x: x, used))
    return solve(b, w, bookset, n)

#################################################### HELPERS



def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0: return inputs
    if mode == 1: return inputs.split()
    if mode == 2: return list(map(int, inputs.split()))

def write(s="\n"):
    if s is None: s = ""
    if isinstance(s, list): s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")

write(main())
