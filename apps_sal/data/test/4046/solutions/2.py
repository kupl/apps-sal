def main():
    n = int(input())
    arr = input().split()
    store = [1]
    mini = 1
    for x in range(n - 1):
        arr[x] = int(arr[x])
        store.append(store[-1] + arr[x])
        mini = min(mini, store[-1])
    for x in range(n):
        store[x] -= mini - 1
    test = store.copy()
    test.sort()
    bo = True
    for x in range(n - 1):
        if test[x + 1] - test[x] != 1:
            bo = False
            break
    if bo:
        for x in range(n):
            print(store[x], end=' ')
    else:
        print(-1)


main()
