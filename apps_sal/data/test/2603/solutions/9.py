for _ in range(int(input())):
    n = int(input())
    ar1 = list(map(int, input().split()))
    ar2 = [e for e in ar1]
    ar2.sort()
    m = ar2[0]
    if any([ar1[i] % m != 0 and ar1[i] != ar2[i] for i in range(n)]):
        print("NO")
    else:
        print("YES")
