n = int(input())
s = [int(i)-1 for i in input().split()]
c = [s[s[s[i]]] for i in range(n)]
for i in range(n):
    if c[i] == i:
        print("YES")
        break
else:
    print("NO")
