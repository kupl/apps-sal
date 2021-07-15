import sys

def main():
    # fin = open("input.txt", "r")
    fin = sys.stdin
    
    n, m = map(int, fin.readline().split())
    A = []
    for i in range(n):
        A.append(fin.readline().rstrip())

    cnt = 0
    for i in range(n - 1):
        for j in range(m - 1):
            S = {A[i][j], A[i][j + 1], A[i + 1][j], A[i + 1][j + 1]}
            if ("f" in S) and ("a" in S) and ("c" in S) and ("e" in S):
                cnt += 1

    print(cnt)

    fin.close()

main()
