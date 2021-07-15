N = int(input())
S = input()
A, B = 0, 0
for i in range(N-10):
    if S[i] == "8":
        A += 1
    else:
        B += 1
if A > B:
    print("YES")
else:
    print("NO")

