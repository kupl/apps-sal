n = int(input())
p = 3
for i in range(n):
    x = 1 << (int(input()) - 1)
    if x & p:
        p ^= 7
        p |= x
    else:
        p = -1
        break
print('YES' if p!=-1 else 'NO')
