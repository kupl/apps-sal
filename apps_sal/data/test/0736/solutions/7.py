# Codeforces Round 272d2 problem A

inp = tuple(map(int, input().split(' ')))
n, m = inp

s1 = n % 2
s2 = n // 2

while (s1+s2) % m != 0 and s2 > 0:
    s2 -= 1
    s1 += 2

if s2 == 0 and s1 % m != 0:
    print(-1)
else:
    print(s1 + s2)
    
    

