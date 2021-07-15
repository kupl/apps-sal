k = int(input())
for i in range(k):
    n = input()
    if int(n[0] * len(n)) <= int(n):
        print(int(n[0]) + (len(n) - 1) * 9)
    else:
        print(int(n[0]) - 1 + (len(n) - 1) * 9)

