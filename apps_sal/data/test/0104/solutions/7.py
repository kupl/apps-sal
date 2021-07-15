n = int(input())
l = list(map(int, input().split()))
s = (sum(l)+1)//2
x = 0
for i in range(len(l)):
    x += l[i]
    if x>=s:
        print(i+1)
        return
