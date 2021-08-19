# author="_rabbit"
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if a[i] == 1:
        b.append(i)
# print(b)
if(len(b) == 0):
    print("0")
else:
    ans = int(1)
    for i in range(len(b) - 1):
        ans = ans * (b[i + 1] - b[i])
    print(ans)
