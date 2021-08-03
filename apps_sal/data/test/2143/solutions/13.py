def main():
    n = int(input())
    sweets = list(map(int, input().split()))
    sweets.sort()
    kids = {}

    for i in range(n):
        for j in range(i + 1, n):
            s = sweets[i] + sweets[j]
            if s not in list(kids.keys()):
                kids[s] = 1
            else:
                kids[s] += 1

    max_kids = 0
    #print (kids)
    for i in list(kids.keys()):
        if kids[i] > max_kids:
            max_kids = kids[i]

    print(max_kids)


main()
