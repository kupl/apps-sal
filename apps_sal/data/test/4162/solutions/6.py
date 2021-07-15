N = int(input())
an = list(map(int,input().split()))

for i in range(N):
    an[i] = an[i] - 1
print(sum(an))
