t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    if n != 1 and m != 1 and n*m != 4:
        print("NO")
    else:
        print("YES")
