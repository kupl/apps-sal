import sys

def solve(A, n, a, b):    
    cost = n*a + (n+1)*b
    num_ones = 0
    groups_ones = 0
    groups_zeros = [0]
    on_zeros = True
    for i in A:
        if i == 0:
            if on_zeros:
                groups_zeros[-1] += 1
            else:
                on_zeros = True
                groups_zeros.append(1)
        else:
            if on_zeros:
                on_zeros = False
                groups_ones += 1
            num_ones += 1
    cost += (groups_ones+num_ones)*b
    for i in range(1, len(groups_zeros)-1):
        z = groups_zeros[i]
        cost += min(2*a, (z-1)*b)
    if num_ones >0 :
        cost += 2*a
    return cost
           
           

in_file = sys.stdin#open("C.txt", "r") 

t = int(in_file.readline().strip())
for _ in range(t):
    n, a, b = map(int, in_file.readline().strip().split())
    A = list(map(int, in_file.readline().strip()))
    sys.stdout.write(str(solve(A, n, a, b)) + "\n")
sys.stdout.flush() 
