N,M = map(int,input().split())
sc = [list(map(int,input().split())) for _ in range(M)]
start = 10**(N-1) if N>1 else 0

for i in range(start,1000):
    count = 0
    for s,c in sc:
        if len(str(i)) >= s:
            if int(str(i)[s-1]) == c:
                count += 1
            else:
                break
    if count == M:
        print(i)
        return

print(-1)
