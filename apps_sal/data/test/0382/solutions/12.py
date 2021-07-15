n,m, q = list(map(int, input().split()))
s = str(input())
t = str(input())

def is_in(index):
    if index + m > n:
        return False
    
    for j in range(m):
        if not t[j] == s[index + j]:
            return False
    return True
        
precalc_ar_2 = [0 for  i in range(n  +1)]
in_was = [ False for i in range(n)]

for i in range(n):
    if is_in(i):
        in_was[i] = True


val = 0
for i in range(1, n + 1):
    if in_was[i - 1]:
        val +=1
    precalc_ar_2[i] = val        


for i in range(q):
    l, r = list(map(int,input().split()))
    if r- m + 1 < 0 or r- m + 1 < l  - 1:
        print(0)
    else:
        print(precalc_ar_2[r - m +1] - precalc_ar_2[l - 1])

