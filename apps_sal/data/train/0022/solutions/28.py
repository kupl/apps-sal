for _ in range(int(input())):
    a, k = list(map(int, input().split()))
    if '0' in str(a):
        print(a)
    else:
        while '0' not in str(a) and k != 1:
            k -= 1
            a += int(max(str(a))) * int(min(str(a)))
        print(a)
