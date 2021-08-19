(p, n) = [int(x) for x in input().split()]
l = [int(input()) for i in range(n)]
table = [False for i in range(p)]
done = False
for i in range(n):
    if table[l[i] % p]:
        print(i + 1)
        done = True
        break
    else:
        table[l[i] % p] = True
if not done:
    print(-1)
