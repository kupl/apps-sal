mp = {}


def main():

    a, b = -1, 0
    n = int(input())
    line = input()  # Read the whole line
    x = line.split()

    for i in range(n):
        a = b
        b = b + int(x[i])
        for k in range(a + 1, b + 1):
            mp[k] = 1 + i

    m = int(input())
    line = input()
    q = line.split()

    for i in range(m):
        print(mp[int(q[i])])


main()
