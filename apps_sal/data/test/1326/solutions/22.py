def main(N):
    x = 0
    for a in range(1, N+1):
        b=N//a
        x += a*b*(b+1)//2
    return x
 
N = int(input())
print(main(N))
