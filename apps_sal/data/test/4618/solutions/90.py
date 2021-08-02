def calc(s, k, n):

    bruh = {}
    for i in range(1, k + 1):  # length
        for j in range(n - (i - 1)):  # start
            bruh[s[j: j + i:]] = 0
    another = bruh.keys()
    another = sorted(another)
    print(another[k - 1])


s = input()

k = int(input())

n = len(s)

calc(s, k, n)
