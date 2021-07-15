def main():
    n, b, a = map(int, input().split())
    arr = list(map(int, input().split()))
    B = b
    A = a
    for i in range(n + 1):
        if (A == 0 and B == 0) or i == n:
            print(i)
            break
        if arr[i]:
            if A == a:
                A -= 1
            elif B:
                B -= 1
                A += 1
            else:
                A -= 1
        else:
            if A:
                A -= 1
            else:
                B -= 1
    return 0

main()
