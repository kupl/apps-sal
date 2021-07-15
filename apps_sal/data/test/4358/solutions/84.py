N = int(input())
p = [int(input()) for i in range(N)]
p = sorted(p)
harai=0

harai = sum(p)-(p[-1]//2)

print(harai)
