N,K = map(int,input().split())

def calculate(n, k):
    print(k * pow(k-1,n-1))

calculate(N, K)
