s = input()
K = int(input())

def substring(S):
    N = len(S)
    ls = []
    for i in range(1,min(6,N+1)):
        for j in range(0,N-i+1):
            ls.append(S[j:j+i])
    setls = set(ls)
    ls = list(setls)
    ls.sort()
    return ls
print(substring(s)[K-1])
