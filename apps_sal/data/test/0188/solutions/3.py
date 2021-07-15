n,k = list(map(int, input().split()))
A = list(map(int, input().split()))

middles = n
sides = n*2
singles = 0

for i,a in enumerate(A):
    s = a//4
    s = min(s, middles)
    middles -= s
    A[i] -= 4*s

for i,a in enumerate(A):
    s = a//2
    s = min(s, sides)
    sides -= s
    A[i] -= 2*s

for i,a in enumerate(A):
    s = a//2
    s = min(s, middles)
    middles -= s
    singles += s
    A[i] -= 2*s

singles += sides
singles += middles*2

for i,a in enumerate(A):
    s = a
    s = min(s, singles)
    singles -= s
    A[i] -= s

rem = sum(A)

if rem == 0:
    print("YES")
else:
    print("NO")


