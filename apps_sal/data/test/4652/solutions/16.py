import sys

def solve(A):
    n = len(A)
    t = A[0]-1
    cw = True
    for a in A:
        if t != a-1:
            cw = False
        t = (t+1)%n
    t = A[0]-1
    ccw = True
    for a in A:
        if t != a-1:
            ccw = False
        t = (n+t-1)%n
    return (ccw or cw)

in_file = sys.stdin #open("A.txt", "r") 

q = int(in_file.readline().strip())
for _ in range(q):
    n = int(in_file.readline().strip())
    A = list(map(int, in_file.readline().strip().split()))
    if solve(A):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
sys.stdout.flush()
