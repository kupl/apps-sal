N = int(input())
a = input().split()
(S, T) = (a[0], a[1])
d = ''
for i in range(N):
    d = d + S[i] + T[i]
print(d)
