n, k = list(map(int, input().split()))
u = list(input())
s = [0] * k
c = ord('A')
for i in range(n):
    s[ord(u[i]) - c] += 1
print(min(s) * k)
   

