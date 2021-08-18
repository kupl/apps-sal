n = int(input())
arra = list(map(int, input().split()))
arrb = list(map(int, input().split()))
arra.sort()
arrb.sort()
a = 0
b = 0
for i in range(2 * n):
    if i % 2 == 0:
        if len(arra) == 0:
            arrb.pop()
        elif len(arrb) == 0 or arra[-1] >= arrb[-1]:
            a += arra[-1]
            arra.pop()
        else:
            arrb.pop()
    else:
        if len(arrb) == 0:
            arra.pop()
        elif len(arra) == 0 or arrb[-1] >= arra[-1]:
            b += arrb[-1]
            arrb.pop()
        else:
            arra.pop()
print(a - b)
'''
n = int(input())
if n == 1 or n == 2:
    print('No')
else: 
    print('Yes')
    print((n + 1) // 2, end = ' ')
    for i in range(1, n + 1, 2):
        print(i, end = ' ')
    print()
    print(n // 2, end = ' ')
    for i in range(2, n + 1, 2):
        print(i, end = ' ')
'''
'''
n, k = map(int, input().split())
s = input()
d = [0 for _ in range(k)]
for i in s:
    d[ord(i) - ord('A')] += 1
print(min(d) * k)
'''
