def solve():

    n = input()

    i = 0
    while n[-i-1] == '0':
        n = '0' + n
        i += 1
    #print(n)

    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            return "NO"
    return "YES"

print(solve())

