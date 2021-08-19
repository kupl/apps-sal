def main():
    (L, R, X, Y, K) = list(map(int, input().split()))
    for i in range(X, Y + 1):
        if L <= i * K <= R:
            ans = 'YES'
            break
    else:
        ans = 'NO'
    print(ans)


main()
