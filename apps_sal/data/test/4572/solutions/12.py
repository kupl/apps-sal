A = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
S = list(set(input()))
for i in S:
    A.remove(i)
A.sort()
try:
    print(A[0])
except:
    print('None')
