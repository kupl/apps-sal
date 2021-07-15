t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    b = list(map(int, input().split()))

    f = [0,0]
    for el in a:
        f[el%2]+=1
    e = [0,0]
    for el in b:
        e[el%2]+=1
    ans.append(e[1]*f[1]+e[0]*f[0])

for el in ans:
    print(el)
