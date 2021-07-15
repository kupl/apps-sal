def AP(seq):
    d = seq[1]-seq[0]
    for i in range(1, len(seq)-1):
        if seq[i+1]-seq[i]!=d:
            return -1
    return d

def main():
    n = int(input())
    s = input().split()
    data = {}
    answer = []

    for i in range(0, len(s)):
        item = s[i]
        if item in data:
            data[item]+=[i]
        else:
            data[item]=[i]

    uniq = [int(item) for item in list(data.keys())]
    uniq.sort()

    for x in uniq:
        iters = data[str(x)]
        count = len(iters)

        if count==1:
            answer.append([x, 0])
            continue
        #else:
        d = AP(iters)
        if d!=-1:
            answer.append([x, d])

    t = len(answer)
    print(t)
    s=''
    for a,b in answer:
        s+=str(a)+' '+str(b)+'\n'
    print(s[:-1])

main()

