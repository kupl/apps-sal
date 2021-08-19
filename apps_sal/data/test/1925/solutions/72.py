
def solve(A, B, N):
    #for x in range(1, N+1): print(f"{x=:2}  {A*x//B=:3} {A*(x//B)}  {A*x//B-A*(x//B)}")
    x = min(B - 1, N)
    a = A * x // B - A * (x // B)
    return a


#solve(10, 12, 25)
A, B, N = list(map(int, input().split()))
#solve(5, 7, 4)
print((solve(A, B, N)))
