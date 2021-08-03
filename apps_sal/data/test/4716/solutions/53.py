#n = int(input())
n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

l.sort(reverse=True)
print((sum(l[:k])))
