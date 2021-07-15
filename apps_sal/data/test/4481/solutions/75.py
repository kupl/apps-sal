N = int(input())

dct = {}

for i in range(N):
    s = input()
    if not s in dct:
        dct[s] = 1

    else:
        dct[s] +=  1
    
m = max(dct.values())
for s in sorted(k for k in dct if dct[k] == m):
    print(s)
