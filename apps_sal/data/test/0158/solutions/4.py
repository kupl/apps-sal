input()
a = sorted(map(int, input().split()))

if a[len(a)//2 -1] < a[len(a)//2]:
    print("YES")
else:
    print("NO")

