n = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)
total = sum(l)
answer = 2*l[0] - total  +1
print(answer)

