c = list(map(int, input().split()))
n, m = map(int, input().split())
p, q = list(map(int, input().split())), list(map(int, input().split()))
print(min(c[3], min(c[2], sum(min(c[0] * i, c[1]) for i in p)) + min(c[2], sum(min(c[0] * i, c[1]) for i in q))))    
