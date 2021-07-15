import sys

def solve():
    n, x0, y0 = read()
    stormtroopers = list()
    for i in range(n):
        xi, yi = read()
        temp = (xi, yi)
        stormtroopers.append(temp)
    shots = 0
    while len(stormtroopers) > 0:
        cur = stormtroopers.pop()
        shots+=1
        if cur[0] - x0 == 0:
            remstormtroopers = [point for point in stormtroopers if point[0] != x0]
        else:
            slope = (cur[1]-y0)/(cur[0]-x0)
            remstormtroopers = [point for point in stormtroopers if abs(point[1] - y0 - slope*(point[0]- x0)) > 0.00001]
        stormtroopers = remstormtroopers
    return shots
    
def read(mode=2):
    inputs = input().strip()
    if mode == 0: return inputs  # String
    if mode == 1: return inputs.split()  # List of strings
    if mode == 2: return list(map(int, inputs.split()))  # List of integers
def write(s="\n"):
    if s is None: s = ""
    if isinstance(s, list): s = " ".join(map(str, s))
    if isinstance(s, tuple): s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")
def run():
    if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
    res = solve()
    write(res)
run()
