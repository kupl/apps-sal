t = input().split(' ')
n = int(t[0])
m = int(t[1])
M = [0] * (n+1)
s = input().split(' ')
for i in s:
    M[int(i)] += 1
sol = M[1]
for j in range(2, len(M)):
    if M[j] < sol:
        sol = M[j]
print(sol)

