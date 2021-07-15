l = list(map(int,input().split()))
n = int(input())
ls = sorted(l)
print(ls[0]+ls[1]+ls[2]*(2**n))
