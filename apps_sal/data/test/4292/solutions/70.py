n,k = map(int,input().split())

p = map(int,input().split())

sp = sorted(p)

score = 0

for i in range(k):
    score += sp[i]

print(score)
