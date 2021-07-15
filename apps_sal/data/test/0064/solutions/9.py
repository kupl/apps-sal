from collections import Counter
n, k = [int(i) for i in input().split()]
s = input()
C = Counter(s)
for c in C:
    if(C[c] > k):
        print("NO")
        break
else:
    print("YES")

