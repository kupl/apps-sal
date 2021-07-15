s, p = map(int,input().split())
for i in range(1, int(p**0.5)+1):
    j = p//i
    if i+j == s and i*j == p:
        print("Yes")
        return
print('No')
