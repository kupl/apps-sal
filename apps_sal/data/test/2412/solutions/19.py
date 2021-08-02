for _ in range(int(input())):
    n = int(input())
    s = input()

    if '8' in s and n - s.find('8') >= 11:
        print("YES")
    else:
        print("NO")
