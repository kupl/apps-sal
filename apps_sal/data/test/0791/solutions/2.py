import sys

def main():
    # fin = open("input.txt", "r")
    fin = sys.stdin
    fout = sys.stdout

    n = int(fin.readline())
    s = list(fin.readline())

    i = 0
    while i < n and s[i] == '1':
        i += 1

    print(min(i + 1, n))


main()
