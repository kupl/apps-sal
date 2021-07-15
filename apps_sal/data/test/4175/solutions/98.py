def readinput():
    n=int(input())
    w=[]
    for _ in range(n):
        w.append(input())
    return n,w

def main(n,w):
    #print(w)
    words={}
    word=w[0]
    words[w[0]] = 1 
    for i in range(1,n):
        #print(w[i])
        if w[i][0]!=word[-1]:
            return 'No'
        else:
            if w[i] not in words:
                words[w[i]] = 1
            else:
                return 'No'
        word = w[i]
    return 'Yes'

def __starting_point():
    n,w=readinput()
    ans=main(n,w)
    print(ans)

__starting_point()
