a = int(input())
for i in range(a):
    input()
    b = list(map(int, input().split()))
    for i in range(len(b) // 2):
        print(- b[i * 2 + 1], b[i * 2], end=" ")
    print()
