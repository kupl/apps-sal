n = int(input())
lst = list(map(int,input().split()))
x = len(lst)
lst = list(set(lst))
y = len(lst)

if (x == y):
    print("YES")
else:
    print("NO")

