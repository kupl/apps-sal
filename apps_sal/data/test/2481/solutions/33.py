from collections import Counter
from itertools import product

def main():
    with open(0) as f:
        H, W = map(int, f.readline().split())
        C = [list(map(int, f.readline().split())) for _ in range(10)] 
        A = Counter(map(int, f.read().split()))

    r10 = range(10)
    for k,i,j in product(r10, r10, r10):
        C[i][j] = min(C[i][j], C[i][k]+C[k][j])

    ans = sum(C[key][1]*value for key,value in A.items() if key != -1)
    print(ans)

main() 
