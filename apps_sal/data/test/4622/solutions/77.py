n = int(input())
alist = list(map(int, input().split()))
if len(set(alist)) == n:
    print("YES")
else:
    print("NO")
