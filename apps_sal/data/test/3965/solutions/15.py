n = int(input())
k = list(map(int,input().split()))
check = 'aeiouy'
for i in range(n):
    s = input()
    ans = 0
    for el in check:
        ans+=s.count(el)
    if ans != k[i]:
        print("NO")
        return
print("YES")
