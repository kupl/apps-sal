def main():
    n = int(input())
    x = sum(map(int, str(n)))
    print("Yes" if n%x==0 else "No")


main()
