t = int(input())
a = list(map(int, input().split()))
s = len(a)
x = s - a[s - 1]
alive = s
for i in range(s - 2, -1, -1):
    if i + 1 >= x:
        alive -= 1
    x = min(x, i - a[i] + 1)
    # print(i,x,alive)
print(alive)
