a = int(input())
for i in range (a):
    b = int(input())
    c = list(map(int, input().split()))
    c.sort()
    def abc(c):
        for j in range (b - 1):
            if c[j] == c[j + 1]:
                return "YES"
        return "NO"
    print(abc(c))
