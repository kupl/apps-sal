t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    even = []
    odd = []
    for i in range(n):
        if s[i] % 2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    if len(even) % 2 == 0:
        print("YES")
    else:
        even = set(even)
        for val in odd:
            if val - 1 in even or val + 1 in even:
                print("YES")
                break
        else:
            print("NO")
