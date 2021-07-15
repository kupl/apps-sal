N = int(input())
A = sorted([int(i) for i in input().split()], reverse=True)
print(sum([A[(i+1)//2] for i in range(N-1)]))
