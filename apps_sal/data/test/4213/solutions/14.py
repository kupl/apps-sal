n = int(input())
li = list(map(int,input().split()))
li.sort()
print(abs(li[-1]-li[0]))
