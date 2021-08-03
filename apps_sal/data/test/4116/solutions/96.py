def kuku(n):
    for i in range(1, 10):
        for j in range(1, 10):
            ans = i * j
            if ans == n:
                print("Yes")
                return 0
    print("No")


n = int(input())

kuku(n)
