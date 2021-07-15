N = int(input())
name = ""
k = 0
p = 0
while(N > p):
    k += 1
    p += 26 ** k
N -= p - 26 ** k + 1
for i in range(k):
    a = N % 26
    N //= 26
    name = chr(a + 97) + name
print(name)
