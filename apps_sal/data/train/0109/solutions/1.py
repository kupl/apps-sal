import math
t = int(input())
M2 = [1]
for i in range(35):
    M2.append(M2[-1]*2)
for i in range(t):
    n, m = map(int,input().split())
    A = list(map(int,input().split()))
    if sum(A) < n:
        print(-1)
    else:
        B = [0] * 33
        for i in range(m):
            B[int(math.log2(A[i]))] += 1
        # print(B[:10])
        C = [0] * 33
        nn = n
        for i in range(33):
            C[i] = nn%2
            nn//=2
            if nn==0:
                break
        # print(C)
        b = 0
        c = 0
        i = 0
        ans = 0
        ok = 0
        while i < len(B):
            while i < len(B) and b >= c:
                b += B[i] * M2[i]
                c += C[i] * M2[i]
                B[i]=0
                i += 1
            if i == len(B) and b >= c:
                print(ans)
                ok = 1
                break
            else:
                i-=1
                while B[i] == 0:
                    i += 1
                    ans += 1
                    # print("ansplus",i)
                B[i] -= 1
                b=0
                c=0
            if ok==1:
                break
