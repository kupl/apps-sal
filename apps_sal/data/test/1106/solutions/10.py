3
n = 2**(int(input())+1)-1
d = input().split(' ')
for i in range(len(d)):
    d[i] = int(d[i])
p = 0
for i in range(len(d)-1, 0, -2):
    p += abs(d[i]-d[i-1])
    d[i//2-1] += max(d[i], d[i-1])
print(p)
