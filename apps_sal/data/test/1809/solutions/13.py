def ans():
    n, m = [int(i) for i in input().split()]
    w = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    books = []
    for i in b:
        if i not in books:
            books.append(i)

    #print(books, w)
    ans = 0
    for i in b:
        arr = books[:books.index(i)]
        #print(i, arr, "h")
        for j in arr:
            ans += w[j - 1]
            #print(i, j, w[i-1], ans)

        books.remove(i)
        books.insert(0, i)

    print(ans)
    return


ans()
