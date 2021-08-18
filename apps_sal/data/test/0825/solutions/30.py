import math
N = int(input())
ans = 0
N_sqrt = int(math.sqrt(N))
primeset = set()
primeset.add(2)
if N == 1:
    print((0))
else:
    for i in range(2, N_sqrt + 5):
        if N % i == 0:
            ans += 1
            nowdiv = 2
            numofdiv = 0
            N //= i
            while(N % i == 0):
                numofdiv += 1
                N //= i
                if numofdiv == nowdiv:
                    ans += 1
                    nowdiv += 1
                    numofdiv = 0
    if N != 1:
        ans += 1
    print(ans)
