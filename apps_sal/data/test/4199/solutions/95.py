N, K = map(int, input().split())
h = list(map(int, input().split()))
def count ():
    count = 0
    for i in range(N):
        if h[i] >= K:
            count +=1
    
    return count
print(count())
