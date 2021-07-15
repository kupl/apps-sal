import sys;input = sys.stdin.readline;print = sys.stdout.write

def main():
    n, m = map(int, input().split())

    arr, have, dpx, dpy, cnt = [0]*n, set(), [0]*n, [0]*m, 0
    for i in range(n):
        arr[i] = input().rstrip()
        for j in range(m):
            if arr[i][j] == "*":
                dpx[i], dpy[j], cnt = dpx[i] + 1, dpy[j] + 1, cnt + 1

    for i in range(n):
        for j in range(m):
            if dpx[i] + dpy[j] - (arr[i][j] == "*") == cnt: print("YES\n{0} {1}".format(i + 1, j + 1)), return

    print("NO")


main()

