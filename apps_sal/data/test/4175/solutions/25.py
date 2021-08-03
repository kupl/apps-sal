def main():
    n = int(input())
    data = [input() for _ in range(n)]

    ok = True
    if len(set(data)) != n:
        ok = False
    for i in range(n - 1):
        if data[i][-1] != data[i + 1][0]:
            ok = False

    print("Yes" if ok else "No")


main()
