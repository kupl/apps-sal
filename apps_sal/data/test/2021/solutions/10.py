n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
s = list(map(int, input().split()))
sum1 = sum(a)
for q in range(m):
    print(sum1-a[s[q]-1])

