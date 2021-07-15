n = int(input())
for i in range(n):
    k = int(input())
    s = list(map(int, input().split()))
    s.sort()
    print(min(k-2,s[k-2]-1))

