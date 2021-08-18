n = int(input())
A = list(map(int, input().split()))
B = []
l = 0
for i in A:
    if i not in B:
        B.append(i)
        l += 1
    if l > 3:
        print("NO")
        return
B.sort()
if l < 3:
    print("YES")
else:
    if B[0] + B[2] == 2 * B[1]:
        print("YES")
    else:
        print("NO")
