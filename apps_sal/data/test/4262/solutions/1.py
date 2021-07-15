import math

def calc(lst):
    ans = 0
    aft = []
    for i in range(N):
        kurai = lst[i]
        aft.append(kurai)

        for j in aft:
            if j < lst[i]:
                kurai -= 1
        
            
        ans = ans + (kurai - 1)*math.factorial(N-(i+1))

    return ans + 1

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

ans = abs(calc(P) - calc(Q))
print(ans)
