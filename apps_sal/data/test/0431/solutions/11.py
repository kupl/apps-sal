import sys

def main():
    n,m = map(int,sys.stdin.readline().split())
    m+=2
    z = []
    for i in range(n):
        z.append(sys.stdin.readline().rstrip())

    ans = 0
    y = n-1
    x = 0
    q = [[x,y,ans]]
    for i in range(n-1,-1,-1):
        first =-1
        last = -1
        for j in range(m):
            if z[i][j] == '1':
                if first == -1:
                    first = j
                last = j
        if first == -1 and last == -1:
            continue
        if i == n-1:
            q[0] = [last,n-1,last]
            continue
        if first == last :
            for t in q:
                t[2]+= min(t[0]+first, m-1-t[0]+m-1-first) + t[1]-i
                t[0] = first
                t[1] = i
            continue
        size = len(q)
        for s in range(size):
            t = q[s]
            q.append([last,i,t[2]+t[0]+last+t[1]-i])
            t[2]+= m-1-t[0]+m-1-first + t[1] - i
            t[0] = first
            t[1] = i
            q[s] = t
    ans = q[0][2]
    for i in range(len(q)):
        if q[i][2] < ans:
            ans = q[i][2]

    print(ans)


main()
