n = int(input())
x = list(map(int, input().split()))
if(len(set(x)) == n):
    print("YES")
else:
    print("NO")
