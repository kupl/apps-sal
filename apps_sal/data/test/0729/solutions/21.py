def main():
    _ = input()
    n = input()
    for i in range(len(n) - 1):
        if n[i] != n[i + 1]:
            print("YES")
            print(n[i:i + 2])
            return
    print("NO")


main()
