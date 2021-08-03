# = list(map(int, input().split()))
# = map(int, input().split())
a = input()
z = list(map(str, input().split()))
n = 5
for i in range(n):
    if a[0] == z[i][0] or a[1] == z[i][1]:
        print("YES")
        return
print("NO")
