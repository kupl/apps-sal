from collections import Counter
import heapq

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cur = n-1
bit = 1
for i in range(n):
    if a[i] == b[i]:
        while a[i]==b[cur] or a[cur]==b[i]:
            if cur == 0:
                bit = -1
            if bit == -1 and cur == n-1:
                print('No')
                return
            cur-=bit
        b[i], b[cur] = b[cur], b[i]
print('Yes')
print((' '.join(list(map(str, b)))))
    
    

