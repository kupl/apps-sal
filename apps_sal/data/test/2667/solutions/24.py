# cook your dish here
t = int(input())
a = list(map(int, input().split()))[:t]
b = (t * (t + 1)) // 2
c = sum(a)
if(b == c):
    print("YES")
else:
    print("NO")
