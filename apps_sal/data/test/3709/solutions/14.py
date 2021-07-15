
n, k = [int(i) for i in input().split()]
s = set([int("".join(input().split()), base=2) for j in range(n)])

for t in s:
    for m in range(1 << k):
        if m in s:
            for i in range(k):
                if ((t >> i) & 1) and ((m >> i) & 1):
                    break
            else:
                print("YES")
                return
                
print("NO")
