for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    wrong0 = sum([1 if a[i] % 2 != i % 2 else 0 for i in range(n) if i % 2 == 0])
    wrong1 = sum([1 if a[i] % 2 != i % 2 else 0 for i in range(n) if i % 2 == 1])
    print(wrong0 if wrong0 == wrong1 else -1)
