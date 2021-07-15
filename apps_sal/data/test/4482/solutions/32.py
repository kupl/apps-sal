n = float(input())

a = list(map(int,input().split()))

ave = round(sum(a)/n)

print(sum(list(map(lambda x:(x-ave)**2,a))))
