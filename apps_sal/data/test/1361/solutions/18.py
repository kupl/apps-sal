def main():
    n = int(input())
    rdl = input().split()
    scp = []
    for i in range(len(rdl)):
        scp.append(int(rdl[i]))
    mn = 10000000
    mx = 0
    maxs = []
    for i in range(len(scp)-1):
        if i != 0:
            mx = 0
            cur  = scp[:i] + scp[i+1:]
            for j in range(len(cur)-1):
                curt = cur[j+1] - cur[j]
                if curt > mx:
                    mx = curt
            maxs.append(mx)
    mn = 1000000
    for i in range(len(maxs)):
        if maxs[i] < mn:
            mn = maxs[i]
    print(mn)
main()

