def ans():
    (n, m) = [int(i) for i in input().split()]
    w = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    books = []
    for i in b:
        if i not in books:
            books.append(i)
    ans = 0
    for i in b:
        arr = books[:books.index(i)]
        for j in arr:
            ans += w[j - 1]
        books.remove(i)
        books.insert(0, i)
    print(ans)
    return


ans()
