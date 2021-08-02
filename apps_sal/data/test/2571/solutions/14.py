for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    print(*[-lst[i + 1] if i % 2 == 0 else lst[i - 1] for i in range(len(lst))])
