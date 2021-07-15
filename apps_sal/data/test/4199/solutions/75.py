n,k =list(map(int, input().split()))

h = list(map(int, input().split()))

# n = int(input())
# s = [map(int, input()) for i in range(3)]

count = 0
for i in range (0,n):
    if h[i] < k:
        count+=1

print((n-count))

