from collections import defaultdict,deque,Counter,OrderedDict

def main():
    n,m,k = map(int,input().split())
    l,ans = [],[]
    for i in range(1,n+1):
        if i%2 == 0:
            for j in range(m,0,-1):
                l.append((i,j))
        else:
            for j in range(1,m+1):
                l.append((i,j))
    curr = 0
    while k > 1:
        ans.append([l[curr][0], l[curr][1], l[curr + 1][0], l[curr + 1][1]])
        curr += 2
        k -= 1
    ans.append([])
    for i in range(curr,len(l)):
        ans[-1].append(l[i][0])
        ans[-1].append(l[i][1])
    for i in ans:
        print(len(i)//2," ".join(map(str,i)))


def __starting_point():
    main()
__starting_point()
