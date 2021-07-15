from sys import stdin, stdout

def main():
    n = int(stdin.readline())
    mat = []
    for i in range(n):
        mat.append(list(map(int, stdin.readline().split())))
    for i in range(n):
        for j in range(n):
            st = True
            for u in range(n):
                for k in range(n):
                    if mat[i][j] == 1 or mat[i][j] == mat[u][j] + mat[i][k]:
                        st = False
                        break
                if not st: break
            if st:
                return False
    return True


print('Yes' if main() else 'No')

