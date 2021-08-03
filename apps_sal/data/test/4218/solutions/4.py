N = int(input())

# N=2n => p=1/2
# N=2n-1 => p=n/N=(N+1)/(2N)
print((N - N // 2) / N)
