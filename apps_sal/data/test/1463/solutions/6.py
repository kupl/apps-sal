import sys


def main():
    n = int(input())
    x = []
    for i in range(n):
        y = list(map(int, sys.stdin.readline().split()))
        x.append(y)

    for i in range(n):
        for j in range(n):
            if x[i][j] == 1:
                continue
            found = False
            for o in range(n):
                a = x[i][o]
                if o == j:
                    continue
                for p in range(n):
                    if p == i:
                        continue
                    b = x[p][j]
                    if a + b == x[i][j]:
                        found = True
                        break
                if found:
                    break
            if not found:
                print("No")
                return
    print("Yes")


main()
