N = int(input())
a = list(map(int,input().split()))

a = [i-1 for i in a]
print(sum(a))
