def main():
    n = int(input())
    a = 2
    while a * a * a < n:
        if n % a == 0:
            b = a + 1
            while b * b < n // a:
                if (n // a) % b == 0:
                    c = n // a // b
                    if a != c and b != c:
                        print("YES")
                        print(a, b, n // a // b)
                        return 0
                b += 1
        a += 1
    print("NO")


p = int(input())
for i in range(p):
    main()
