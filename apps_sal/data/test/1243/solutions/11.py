n = int(input())
t = list(map(int, input().split()))
s = sum(t)//n
t = [i-s for i in t]
r = 0
for i in range(len(t) - 1):
    t[i+1] += t[i]
    r += abs(t[i])

print(r)
